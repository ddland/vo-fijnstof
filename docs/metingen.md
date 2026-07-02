# Metingen

Nu de libraries zijn geïnstalleerd, kun je metingen uitvoeren.

## Weergave van data in Thonny

Lees de meetwaarden van de sensor uit en geef ze weer in de Shell van Thonny. De code kan worden gekopieerd naar het `editor`-scherm van Thonny. Daarna kun je de code uitvoeren met de groene `run`-knop.

``` {literalinclude} ../voorbeelden/meting_weergave.py
```

Als de Raspberry Pi Pico is aangesloten en MicroPython is gekozen als Python-versie, verschijnen er regels met meetwaarden:

```
tijd [s];pm 1.0 [ug/m3];pm 2.5 [ug/m3];pm 4.0 [ug/m3];pm 10 [ug/m3];temp [degC];rel. hum [%];CO2 [ppm]
1782855955;0.9;1.9;2.7;3.1;27.285;44.85;673
1782855960;0.9;1.9;2.7;3.1;27.29;44.85;680
```

De eerste kolom is de tijd. Deze staat in seconden sinds 1 januari 1970. Dit heet een [Unix-timestamp](https://en.wikipedia.org/wiki/Unix_time). De volgende vier kolommen zijn de PM1.0-, PM2.5-, PM4.0- en PM10-waarden. Daarna volgen de temperatuur in graden Celsius, de relatieve luchtvochtigheid en de concentratie $CO_2$ in ppm.

## Metingen opslaan op de Raspberry Pi Pico

Om de data in een bestand op te slaan, moet er een bestand op de Raspberry Pi Pico worden aangemaakt. Dan kun je de waarden later opnieuw gebruiken. In dit voorbeeldscript wordt een bestand met de naam `meting_000.csv` aangemaakt. Als dit bestand al bestaat, wordt de volgende naam geprobeerd: `meting_001.csv`. Dit gaat zo door totdat er een bestandsnaam is gevonden die nog niet bestaat.

Na de metingen kan de Raspberry Pi Pico weer met de computer worden verbonden via Thonny. Daarna kun je het meetbestand downloaden naar de computer. Klik daarvoor met de rechtermuisknop op de bestandsnaam in het `Raspberry Pi`-deel van de bestanden in Thonny.

``` {literalinclude} ../voorbeelden/meting_opslaan.py
```

## Weergave op OLED-scherm

Door een OLED-scherm ([128x64](https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/) of [64x64](https://wiki.seeedstudio.com/Grove-OLED-Display-0.66-SSD1306_v1.0/)) aan de Raspberry Pi Pico aan te sluiten, kunnen meetgegevens op het scherm worden weergegeven. Ook kan de status van de meting worden bijgehouden, of kan er feedback worden gegeven aan de gebruiker van het meetsysteem.

``` {literalinclude} ../voorbeelden/meting_oled.py
```

## Koppeling met GPS-sensor

Met een GPS-unit kan de locatie van de sensor op elk moment worden opgeslagen. Door deze data tegelijk met de sensordata naar een bestand te schrijven, kun je achteraf zien op welke locatie de blootstelling is gemeten.

``` {literalinclude} ../voorbeelden/meting_gps.py
```
