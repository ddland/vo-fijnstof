# Metingen
Nu de libraries geinstalleerd zijn is het mogelijk om metingen uit te voeren. 

## Weergave van data in Thonny
Leest de meetwaarden van de sensor uit en geeft die weer in de Shell van Thonny. De code kan gekopieerd worden naar het `editor` scherm van Thonny en dan met de groene `run` knop worden uitgevoerd. 

``` {literalinclude} ../voorbeelden/meting_weergave.py
```
Als de Raspberrypi Pico is aangesloten en micropython gekozen is als Python versie zouden er regels met meetwaarden moeten verschijnen:
```
tijd [s];pm 1.0 [ug/m3];pm 2.5 [ug/m3];pm 4.0 [ug/m3];pm 10 [ug/m3];temp [degC];rel. hum [%];CO2 [ppm]
1782855955;0.9;1.9;2.7;3.1;27.285;44.85;673
1782855960;0.9;1.9;2.7;3.1;27.29;44.85;680
```
De eerste kolom de tijd (in seconden sinds 1 januari 1970, de [unix-timestamp](https://en.wikipedia.org/wiki/Unix_time)). De volgende vier zijn de PM1.0, PM2.5, PM4.0 en PM10 waarden. Daarna de temperature (in graden Celcius) en de concentratie $CO_2$, in deeltjes-per-miljoen.

## Metingen opslaan op de Raspberrypi Pico
Om de data in een bestand op te slaan (zodat je later de waarden nog kan gebruiken) moet er een bestand op de Raspberrypi Pico aangemaakt worden waarin de data opgeslagen (of geprint) kan worden. In dit voorbeeld script wordt er een file `meting_000.csv` aangemaakt. Als het bestand al bestaat wordt de volgende (`meting_001.csv`) geprobeerd, netzolang totdat er een file aangemaakt kan worden die nog niet bestaat. 

Na de metingen kan de Raspberrypi Pico weer verbonden worden met de computer doormiddel van Thonny. Daarna kan, door recht-klikken op de bestandsnaam in het `Raspberrypi` deel van de files (of bestanden) in Thonny het metingen bestand gedownload worden naar de computer. 
``` {literalinclude} ../voorbeelden/meting_opslaan.py
```


## Weergave op OLED scherm
Door een OLED scherm ([128x64](https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/) of [64x64](https://wiki.seeedstudio.com/Grove-OLED-Display-0.66-SSD1306_v1.0/) aan de Raspberrypi Pico aan te sluiten kunnen op het scherm meetdata weergegeven worden. Ook kan de status van de meting bijgehouden worden of feedback gegegevn worden aan de gebruiker van het meetsysteem.
``` {literalinclude} ../voorbeelden/meting_oled.py
```

## Koppeling met GPS sensor
Met een GPS unit kan de locatie van de sensor op elk moment verwerkt worden. Door deze data gelijktijdig met de sensor data weg te schrijven naar een bestand kan achteraf de locatie van de blootstelling weergegeven worden.
``` {literalinclude} ../voorbeelden/meting_gps.py
```

## Toegang tot Pico via WiFi 
``` {literalinclude} ../voorbeelden/meting_wifi.py
```


