#!/usr/bin/python
import socket, sys, urllib2;


###################
## Configuration ##
###################
IBOX_MODEL = "80 00 00 00 11"   # iBox2
IBOX_IP = "192.168.1.18"        # iBox2 IP address
UDP_PORT_SEND = 5987            # Port for sending
UDP_PORT_RECEIVE = 55054        # Port for receiving
UDP_MAX_TRY = 5                 # Max sending
UDP_TIMEOUT = 5                 # Wait for data in sec
DOMOTICZ_IP = "192.168.1.17"    # Domoticz IP only needed for logging
DOMOTICZ_LOG = 0                # Turn logging to Domoticz on/off 0=off and 1=on
############################################################################################################


#####################	
## Log to Domoticz ##
#####################
def doLog(MSG):
    try:
        if DOMOTICZ_LOG == 1:
            urllib2.urlopen("http://"+DOMOTICZ_IP+"/json.htm?type=command&param=addlogmessage&message="+MSG.replace(" ", "%20")).read()

    except Exception as ex:
        print "[DEBUG] log error                :", ex 


#########################
## iBox2 bulb commands ##
#########################
def iBox2BulbCommand(x):
    return {
		"COLOR001"       : "31 00 00 08 01 BA BA BA BA",
		"COLOR002"       : "31 00 00 08 01 FF FF FF FF",
		"COLOR003"       : "31 00 00 08 01 7A 7A 7A 7A",
		"COLOR004"       : "31 00 00 08 01 1E 1E 1E 1E",
		"SATUR00"        : "31 00 00 08 02 64 00 00 00",
		"SATUR25"        : "31 00 00 08 02 4B 00 00 00",
		"SATUR50"        : "31 00 00 08 02 32 00 00 00",
		"SATUR75"        : "31 00 00 08 02 19 00 00 00",
		"SATUR100"       : "31 00 00 08 02 00 00 00 00",
		"DIM00"          : "31 00 00 08 03 64 00 00 00",
		"DIM25"          : "31 00 00 08 03 4B 00 00 00",
		"DIM50"          : "31 00 00 08 03 32 00 00 00",
		"DIM75"          : "31 00 00 08 03 19 00 00 00",
		"DIM100"         : "31 00 00 08 03 00 00 00 00",
		"ON"             : "31 00 00 08 04 01 00 00 00",
		"OFF"            : "31 00 00 08 04 02 00 00 00",
		"NIGHTON"        : "31 00 00 08 04 05 00 00 00",
		"SPEEDUP"        : "31 00 00 08 04 03 00 00 00",
		"SPEEDDOWN"      : "31 00 00 08 04 04 00 00 00",
		"WHITEON"        : "31 00 00 08 05 64 00 00 00",		
		"WW00"           : "31 00 00 08 05 64 00 00 00",
		"WW25"           : "31 00 00 08 05 4B 00 00 00",
		"WW50"           : "31 00 00 08 05 32 00 00 00",
		"WW75"           : "31 00 00 08 05 19 00 00 00",
		"WW100"          : "31 00 00 08 05 00 00 00 00",
		"MODE01"         : "31 00 00 08 06 01 00 00 00",
		"MODE02"         : "31 00 00 08 06 02 00 00 00",
		"MODE03"         : "31 00 00 08 06 03 00 00 00",
		"MODE04"         : "31 00 00 08 06 04 00 00 00",
		"MODE05"         : "31 00 00 08 06 05 00 00 00",
		"MODE06"         : "31 00 00 08 06 06 00 00 00",
		"MODE07"         : "31 00 00 08 06 07 00 00 00",
		"MODE08"         : "31 00 00 08 06 08 00 00 00",
		"MODE09"         : "31 00 00 08 06 09 00 00 00",
	}.get(x)


###########################
## iBox2 command builder ##
###########################
def iBox2CommandBuilder(iBoxModel, iBoxSessionID1, iBoxSessionID2, iBoxCycleNR, lightCommand, lightZone, checkSum, Splitter):
	return iBoxModel + " " + iBoxSessionID1 + " " + iBoxSessionID2 + " " + Splitter + " " + iBoxCycleNR + " " + Splitter + " " + lightCommand + " " + lightZone + " " + Splitter + " " + checkSum


######################
## Checksum builder ##
######################
def getChecksum(data):
	checksum = 0
	for x in bytearray.fromhex(data):
		checksum += x
	return format(checksum, "04X")[2:]


##########################
## Commandline commands ##
##########################
CMDLINE_INFO = (
"##########################\n"
"## Command line options ##\n"
"##########################\n"
"Use command line as follow : milight.py CMD1 CMD2\n"
"                           : CMD1 Bulb zone\n"
"                           : CMD2 Bulb command\n"
"-------------------------------------------------------------------------------\n"
"Select the bulb zone       : 00 01 02 03 04\n"
"Bulb on/off                : ON OFF NIGHTON WHITEON\n"
"Mode Speed up/down         : SPEEDUP SPEEDDOWN\n"
"Kelvin warmwhite           : WW00 WW25 WW50 WW75 WW100\n"
"Brightness                 : DIM00 DIM25 DIM50 DIM75 DIM100\n"
"Saturation                 : SATUR00 SATUR25 SATUR50 SATUR75 SATUR100\n"
"Mode (discomode)           : MODE01 MODE02 MODE03 MODE04 MODE05\n"
"                           : MODE06 MODE07 MODE08 MODE09\n"
"Bulb color                 : COLOR001 COLOR002 COLOR003 COLOR004\n"
)

try:
    CMDLINE_ZONE = sys.argv[1].strip()
    print "[DEBUG] start command1           :", CMDLINE_ZONE

    CMDLINE_CMD = sys.argv[2].strip()
    print "[DEBUG] start command2           :", CMDLINE_CMD

except:
    print CMDLINE_INFO
    raise SystemExit()
doLog("milight script started (milight.py " + CMDLINE_ZONE + " " + CMDLINE_CMD + ")")


###################
## Start session ##
###################
Session = False
for iCount in range(0, UDP_MAX_TRY):
    try:
        START_SESSION = "20 00 00 00 16 02 62 3A D5 ED A3 01 AE 08 2D 46 61 41 A7 F6 DC AF D3 E6 00 00 1E"
        doLog("milight script starting ibox session...")
        sockServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sockServer.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sockServer.bind(('', UDP_PORT_RECEIVE))
        sockServer.settimeout(UDP_TIMEOUT)
        sockServer.sendto(bytearray.fromhex(START_SESSION), (IBOX_IP, UDP_PORT_SEND))
        dataReceived, addr = sockServer.recvfrom(1024)
        dataResponse = str(dataReceived.encode('hex')).upper()
        SessionID1 = dataResponse[38:40]
        SessionID2 = dataResponse[40:42]
        print "[DEBUG] iBox model               :", IBOX_MODEL
        print "[DEBUG] received session message :", dataResponse
        print "[DEBUG] sessionID1               :", SessionID1
        print "[DEBUG] sessionID2               :", SessionID2
        Session = True
        break

    except socket.timeout:
        print "[DEBUG] timeout on session start :", START_SESSION
        doLog("milight script timeout on command... doing a retry")
        sockServer.close()
        continue

    except Exception as ex:
        print "[DEBUG] something's wrong        :", ex 
        doLog("milight script something's wrong with the session...")


#######################
## Send bulb command ##
#######################
if Session == True:
    for iCount in range(0, UDP_MAX_TRY):
        try:
            CycleNR = str(iCount).zfill(2)
            print "[DEBUG] cycle number             :", CycleNR

            bulbCommand = iBox2BulbCommand(CMDLINE_CMD)
            print "[DEBUG] light command            :", bulbCommand

            Checksum = getChecksum(bulbCommand + "00" + CMDLINE_ZONE)
            print "[DEBUG] checksum                 :", Checksum

            sendCommand = iBox2CommandBuilder(IBOX_MODEL, SessionID1, SessionID2, CycleNR, bulbCommand, CMDLINE_ZONE, Checksum, "00")
            print "[DEBUG] sending command          :", sendCommand
            doLog("milight script send bulb command: " + sendCommand)

            sockServer.sendto(bytearray.fromhex(sendCommand), (IBOX_IP, UDP_PORT_SEND))
            dataReceived, addr = sockServer.recvfrom(1024)
            dataResponse = str(dataReceived.encode('hex')).upper()
            print "[DEBUG] received message         :", dataResponse
            doLog("milight script received from bulb: " + dataResponse)
            break

        except socket.timeout:
            print "[DEBUG] timeout on command       :", sendCommand
            doLog("milight script timeout on command... doing a retry")
            continue

        except Exception as ex:
            print "[DEBUG] something's wrong        :", ex
            doLog("milight script something's wrong with te command...")

        finally:
            sockServer.close()
else:
    sockServer.close()

doLog("milight script ready...")
raise SystemExit()
