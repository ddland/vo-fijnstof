# Metingen

Nu de libraries zijn geïnstalleerd, kun je metingen uitvoeren. All de voorbeelden staan ook in de folder [voorbeelden](https://github.com/ddland/vo-fijnstof/tree/main/voorbeelden) van het github-repository.

Let erop dat de hardware juist is aangesloten. De software gaat er vanuit dat de sensoren op GPIO-0 en GPIO-1 aangesloten zijn. Als dat niet het geval is, pas de code aan! Door de voorgeschreven SDA/SCL pinnen van de Raspberry Pi Pico te gebruiken kan de snelle, hardware, implementatie gebruikt worden. Als er andere pinnen gebruikt worden moet de softwere I2C bibliotheek, `SoftI2C` uit de `machine` module gebruikt worden. 

## Weergave van data in Thonny

Lees de meetwaarden van de sensor uit en geef ze weer in de Shell van Thonny. De code kan worden gekopieerd naar het `editor`-scherm van Thonny. Daarna kun je de code uitvoeren met de groene `run`-knop.

``` {literalinclude} ../voorbeelden/meting_weergave.py
```

Als de Raspberry Pi Pico is aangesloten en MicroPython is gekozen als Python-versie, verschijnen er regels met meetwaarden:
```
tijd [s];pm 1.0 [ug/m3];pm 2.5 [ug/m3];pm 4.0 [ug/m3];pm 10 [ug/m3];temp [degC];rel. hum [%];CO2 [ppm]
1783375431;6553.5;6553.5;6553.5;6553.5;28.315;46.72;32767
1783375436;0.2;0.2;0.2;0.3;28.315;46.72;32767
1783375441;0.3;0.4;0.4;0.4;28.295;46.71;32767
1783375446;0.3;0.4;0.4;0.4;28.2;46.7;32767
1783375451;0.5;0.6;0.7;0.7;27.825;46.71;32767
1783375456;0.5;0.7;0.8;0.8;27.045;46.75;790
1783375461;0.7;0.9;1.0;1.1;26.39;47.47;637
``` 

De eerste kolom is de tijd. Deze staat in seconden sinds 1 januari 1970. Dit heet een [Unix-timestamp](https://en.wikipedia.org/wiki/Unix_time). De volgende vier kolommen zijn de PM1.0-, PM2.5-, PM4.0- en PM10-waarden. Daarna volgen de temperatuur in graden Celsius, de relatieve luchtvochtigheid en de concentratie $CO_2$ in ppm.
De eerste regel kan onjuiste data teruggeven. De sensor geeft als eerste waarden de maximale waarden terug. Het is niet zo dat de fijnstof concentratie extreem hoog was, die meetpunten kunnen uit de dataset gehaald worden. 

## Metingen opslaan op de Raspberry Pi Pico

Om de data in een bestand op te slaan, moet er een bestand op de Raspberry Pi Pico worden aangemaakt. Dan kun je de waarden later opnieuw gebruiken. In dit voorbeeldscript wordt een bestand met de naam `meting_000.csv` aangemaakt. Als dit bestand al bestaat, wordt de volgende naam geprobeerd: `meting_001.csv`. Dit gaat zo door totdat er een bestandsnaam is gevonden die nog niet bestaat.

``` {literalinclude} ../voorbeelden/meting_opslaan.py
```

Na de metingen kan de Raspberry Pi Pico weer met de computer worden verbonden via Thonny. Daarna kun je het meetbestand downloaden naar de computer. Klik daarvoor met de rechtermuisknop op de bestandsnaam in het `Raspberry Pi`-deel van de bestanden in Thonny.
Een voorbeeld dataset staat in [voorbeelden/data](https://github.com/ddland/vo-fijnstof/tree/main/voorbeelden/data/meeting_001.csv), `meting_001.csv`. Het format is hetzelfde als hierboven weergegeven, punt-komma gescheiden data met als eerste regel de beschrijving van de datapunten. Een voorbeeld van weergave van de data is in het [analyse](../analyse.md) hoofdstuk weergegeven.  

## Weergave op OLED-scherm

Door een OLED-scherm ([128x64](https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/) of [64x64](https://wiki.seeedstudio.com/Grove-OLED-Display-0.66-SSD1306_v1.0/)) aan de Raspberry Pi Pico aan te sluiten, kunnen meetgegevens op het scherm worden weergegeven. Ook kan de status van de meting worden bijgehouden, of kan er feedback worden gegeven aan de gebruiker van het meetsysteem.

``` {literalinclude} ../voorbeelden/meting_oled.py
```
De driver (ssd1306.py) staat al in de [lib](https://github.com/ddland/vo-fijnstof/tree/main/lib) folder. Als alle files al naar de `lib` folder op de Raspberry Pi Pico gekopieerd zijn dan kan het voorbeeld script direct uitgevoerd worden. 

## Koppeling met GPS-sensor

Met een GPS-unit kan de locatie van de sensor op elk moment worden opgeslagen. Door deze data tegelijk met de sensordata naar een bestand te schrijven, kun je achteraf zien op welke locatie de blootstelling is gemeten.

``` {literalinclude} ../voorbeelden/meting_gps.py
```
