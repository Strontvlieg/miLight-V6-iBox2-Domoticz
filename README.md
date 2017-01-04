# miLight-V6-iBox2-Domoticz
Controls your miLights iBox2 V6 with Domoticz<br/>
Test with bulbs RGBW/WW/CW 

<h4>Use as follow: milight.sh CMD1 CMD2</h4>

<h4>CMD1 Bulb zone</h4>
<p>
00 01 02 03 04
</p>
<h4>CMD2 Bulb commands</h4>
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
--------------------------<br/>
-- Command line options --<br/>
--------------------------<br/>
Use command line as follow : milight.sh CMD1 CMD2<br/>
                           : CMD1 Bulb zone<br/>
                           : CMD2 Bulb command<br/>
-------------------------------------------------------------------------------------------<br/>
Select the bulb zone       : 00 01 02 03 04<br/>
Bulb on/off                : ON OFF NIGHTON WHITEON<br/>
Kelvin warmwhite           : WW00 WW25 WW50 WW75 WW100<br/>
Brightness                 : DIM00 DIM25 DIM50 DIM75 DIM100<br/>
Saturation                 : SATUR00 SATUR25 SATUR50 SATUR75 SATUR100<br/>
Mode (discomode)           : MODE01 MODE02 MODE03 MODE04 MODE05 MODE06 MODE07 MODE08 MODE09<br/>
Mode Speed up/down         : SPEEDUP SPEEDDOWN<br/>
<br/>
