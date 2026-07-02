# SPS30

De sensor moet worden aangesloten op de 5V-aansluiting van de Raspberry Pi Pico. Houd de sensor met de groene kant onder. Als je dan naar de rand van de sensor kijkt, ziet die er zo uit:

```
 ---------------
 |       12345 |
 | *  *   *  * |
 ---------------
```

Pin 1 tot en met 5 zijn dan:

1. VDD (5V)
2. SDA
3. SCL
4. GND (voor I2C)
5. GND

Pin 4 moet, net als pin 5, met GND verbonden zijn om de I2C-aansluiting van de sensor te gebruiken.

