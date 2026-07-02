# SEN63-C

De sensor moet via de 3.3V aansluiting van de Raspberry Pi Pico aangesloten worden. Kijkend naar de sensor met de barcode sticker aan de bovenkant zien de aansluitingen er zo uit:
```
 -------------------
 |   --   [barcode]|
 |  /  \           |
 |  \  /--------|  |
 |   --  123456 |  |
 -------------------
```

Pin 1 tot en met 6 zijn dan:
1. VDD (3.3V)
2. GND
3. SCL
4. SDA
5. GND
6. VDD (3.3V)

De VDD en GND pinnen zijn dubbel uitgevoerd, daar hoeven er maar 1 van aangesloten te worden.
De software om de sensor met een Raspberry Pi Pico uit te lezen staat in de lib directory van dit repositorie. 

Voor gebruik moet de `meting_sen63c.py` en de `sen6x.py` file naar de `lib` folder op de Raspberry Pi Pico geupload worden. 

Het bestand `meting_sen63c.py` is zo gemaakt dat deze alleen de PM1.0, PM2.5, PM4.0, PM10 temperatuur, relatieve luchtvochtigheid en $CO_2$ waarden teruggeeft. Daarnaast begint de sensor eerst met een schoonmaak routine zodra het bestand uitgevoerd wordt.

