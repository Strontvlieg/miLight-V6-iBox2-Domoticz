# miLight-V6-iBox2-Domoticz
Control your miLights iBox2 V6 with Domoticz

Use as follow: milight.sh CMD1 CMD2

CMD1 Bulb zone
00 01 02 03 04

CMD2 Bulb commands 
ON OFF NIGHTON WHITEON WW00 WW25 WW50 WW75 WW100 DIM00 DIM25 DIM50 DIM75 DIM100 SATUR00 SATUR25 SATUR50 SATUR75 SATUR100 MODE01 MODE02 MODE03 MODE04 MODE05 MODE06 MODE07 MODE08 MODE09 SPEEDUP SPEEDDOWN

Domoticz example ON/OFF switch
1. Add a virtual/dummy switch in Domoticz (see https://www.domoticz.com/wiki/Wemo#Creating_Dummy_Switches)
2. The ON action of the dummy switch should be set to: script:///home/pi/domoticz/scripts/python/milight.sh 00 ON
3. The OFF action of the dummy switc should be set to: script:///home/pi/domoticz/scripts/python/milight.sh 00 OFF
