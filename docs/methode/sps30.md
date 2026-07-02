# SPS30

De sensor moet via de 5V aansluiting van de Raspberry Pi Pico aangesloten worden. Met de groene kant onder en kijkend naar de sensor ziet de zijkant er zo uit:
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

Pin 4 moet net als pin 5 met de GND verbonden zijn om de I2C aansluiting van de sensor te gebruiken. 
De software om de sensor met een Raspberry Pi Pico uit te lezen staat in de lib directory van dit repositorie. 

Voor gebruik moet de `meting_sps30.py` en de `sps30.py` file naar de `lib` folder op de Raspberry Pi Pico geupload worden. Daarna kunnen de `sps_...py` files gebruikt worden, afhankelijk van de toepassing. 
Door deze files te hernoemen naar `main.py` worden ze bij opstarten van de Raspberry Pi Pico gelijk uitgevoerd. Op die manier is het mogelijk zonder computer in de buurt toch gebruik te maken van de sensor. 

Het bestand `meting_sps30.py` is zo gemaakt dat deze alleen de PM1.0, PM2.5, PM4.0 en PM10 waarden teruggeeft. Daarnaast begint de sensor eerst met een schoonmaak routine zodra het bestand uitgevoerd wordt.

