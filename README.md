# miLight iBox2 control for Domoticz
Controls your miLights bulbs and iBox2 with Domoticz and retry commands when sending fails.<br/>
Tested with bulbs RGBW/WW/CW<br/>
<img src="http://stair-lighting.com/images/MI-LIGHT/WiFi-iBox2/mini/250px_wifi-ibox2-1.jpg">
<h4>How to install</h4>
<p>
Copy milight.py to /home/pi/domoticz/scripts/python and set chmod to 777 on the files<br/>
Change the follow setting to your own settings with Notepad++<br/>
<ul>
  <li>IBOX_IP = "192.168.1.18"</li>
  <li>IBOX_MODEL = "80 00 00 00 11" # iBox2</li>
  <li>UDP_PORT_SEND = 5987</li>
  <li>UDP_PORT_RECEIVE = 55054</li>
  <li>UDP_MAX_TRY = 3</li>
  <li>UDP_TIMEOUT = 5</li>
</ul>
</p>
<h4>How to use</h4>
<p>
/home/pi/domoticz/scripts/python/milight.py CMD1 CMD2
</p>
<h4>CMD1 = Bulb zone</h4>
<p>
00 01 02 03 04
</p>
<h4>CMD2 = Bulb command</h4>
<p>
ON OFF NIGHTON WHITEON WW00 WW25 WW50 WW75 WW100 DIM00 DIM25 DIM50 DIM75 DIM100 SATUR00 SATUR25 SATUR50 SATUR75 SATUR100 MODE01 MODE02 MODE03 MODE04 MODE05 MODE06 MODE07 MODE08 MODE09 SPEEDUP SPEEDDOWN
</p>
<h4>Domoticz example ON/OFF switch</h4>
<p>
<ol>
  <li>Add a virtual/dummy switch in Domoticz (see https://www.domoticz.com/wiki/Wemo#Creating_Dummy_Switches)</li>
  <li><b>ON action dummy switch:</b> script:///home/pi/domoticz/scripts/python/milight.py 00 ON</li>
  <li><b>OFF action dummy switch:</b> script:///home/pi/domoticz/scripts/python/milight.py 00 OFF</li>
</ol>
</p>
<h4>Command line options</h4>
<p>
<table>
<tr>
<td>Bulb zone</td>
<td>00 01 02 03 04</td>
</tr>
<tr>
<td>Bulb on/off</td>
<td>ON OFF NIGHTON WHITEON</td>
</tr>
<tr>
<td>Kelvin warmwhite</td>
<td>WW00 WW25 WW50 WW75 WW100</td>
</tr>
<tr>
<td>Brightness</td>
<td>DIM00 DIM25 DIM50 DIM75 DIM100</td>
</tr>
<tr>
<td>Saturation</td>
<td>SATUR00 SATUR25 SATUR50 SATUR75 SATUR100</td>
</tr>
<tr>
<td>Mode (discomode)</td>
<td>MODE01 MODE02 MODE03 MODE04 MODE05 MODE06 MODE07 MODE08 MODE09</td>
</tr>
<tr>
<td>Mode Speed up/down</td>
<td>SPEEDUP SPEEDDOWN</td>
</tr>
</table>
</p>
