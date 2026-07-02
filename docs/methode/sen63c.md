# SEN63-C

De sensor moet worden aangesloten op de 3,3V-aansluiting van de Raspberry Pi Pico. Als je naar de sensor kijkt met de barcodesticker aan de bovenkant, zien de aansluitingen er zo uit:

```
 -------------------
 |   --   [barcode]|
 |  /  \           |
 |  \  /--------|  |
 |   --  123456 |  |
 -------------------
```

Pin 1 tot en met 6 zijn dan:

1. VDD (3,3V)
2. GND
3. SCL
4. SDA
5. GND
6. VDD (3,3V)

De VDD- en GND-pinnen zijn dubbel uitgevoerd. Je hoeft van elk maar één pin aan te sluiten.

