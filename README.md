# miLight-V6-iBox2-Domoticz
Controls your miLights iBox2 V6 with Domoticz<br/>
Tested with bulbs RGBW/WW/CW<br/>
<img src="http://stair-lighting.com/images/MI-LIGHT/WiFi-iBox2/mini/250px_wifi-ibox2-1.jpg">

<h4>Use as follow: milight.sh CMD1 CMD2</h4>

<h4>CMD1 Bulb zone</h4>
<p>
00 01 02 03 04
</p>
<h4>CMD2 Bulb command</h4>
<p>
ON OFF NIGHTON WHITEON WW00 WW25 WW50 WW75 WW100 DIM00 DIM25 DIM50 DIM75 DIM100 SATUR00 SATUR25 SATUR50 SATUR75 SATUR100 MODE01 MODE02 MODE03 MODE04 MODE05 MODE06 MODE07 MODE08 MODE09 SPEEDUP SPEEDDOWN
</p>
<h4>Domoticz example ON/OFF switch</h4>
<p>
<ol>
<li>Add a virtual/dummy switch in Domoticz (see https://www.domoticz.com/wiki/Wemo#Creating_Dummy_Switches)</li>
<li>ON action dummy switch: script:///home/pi/domoticz/scripts/python/milight.sh 00 ON</li>
<li>OFF action dummy switch: script:///home/pi/domoticz/scripts/python/milight.sh 00 OFF</li>
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
