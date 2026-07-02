# Methode

De fijnstof sensoren ([Sensirion SPS30](https://sensirion.com/products/catalog/SPS30), [SEN63-C](https://sensirion.com/products/catalog/SEN63C)) maken met behulp van licht-verstrooing het mogelijk de hoeveelheid deeltjes met een bepaalde grote te tellen. Deze waarden worden dan omgezet in massa fijnstof per volume ($\mu$g/m$^3$). De sensor kan ook andere waarden weergeven, maar voor nu laten we het bij de massa per volume. Als je de handleiding van de sensor goed doorleest zie je zelfs dat de sensor de PM4.0 en PM10 waarden niet meet, maar aan de hand van de andere waarden berekent. De nauwkeurigheid is welke spreiding de sensor mag aangeven bij het meten van dezelfde concentratie. Heb je meerdere sensoren dan kan je bij dezelfde blootstelling, binnen deze grenzen, meetwaarden verwachten. 

De sensoren geven de volgende waarden terug voor de fijnstof metingen:


| naam  | grootte bereik    | nauwkeurigheid                |
--------|-------------------|-------------------------------|
| PM1.0 | 0.3 - 1.0 um  | 5 $\mu g/m^3$ + 5% meetwaarde |
| PM2.5 | 0.3 - 2.5 um  | 5 $\mu g/m^3$ + 5% meetwaarde |
| PM4.0 | 0.3 - 4.0 um  | 25 $\mu g/m^3$                |
| PM10  | 0.3 - 10.0 um | 25 $\mu g/m^3$                |

Daarnaast meet de SEN63-C ook de temperatuur, luchtvochtigheid en $CO_2$ concentratie. Deze metingen ontbreken bij de SPS30, die alleen fijnstof meet. Het meten van luchtvochtigheid maakt het mogelijk om te compenseren voor de interactie van fijnstof met de luchtvochtigheid. Afhankelijk van de diepgang van je onderzoeks vraag kan je daar rekening mee houden. 

## Software
De software voor de sensoren staat in de [library folder](../lib/). Deze software is zo geschreven dat je altijd de volgende output van de sensoren terugkrijgt:
```
tijd [s]; pm1.0 [ug/m3]; pm2.5 [ug/m3]; pm4.0 [ug/m3]; pm10 [ug/m3]; temperatuur [degC];  rel. luchtvochigheid [%]; CO2 [ppm]
```
De files `sen6x.py` en `sps30.py` bevatten de code die noodzakelijk is om de hardware aan te sturen. Hier worden de commmando's naar de sensor gestuurd om een meting uit te voeren. De files `meting_sen6x.py` en `meting_sps30.py` zorgen ervoor dat de output van de sensoren er hetzelfde uitziet. Als er met een SPS30 gemeten wordt zullen er evenveel data-elementen teruggegeven worden, maar niet elke waarde is gemeten. De SPS30 meet geen temperatuur, luchtvochtigheid en $CO_2$ en zal daarom daar `NaN` terugggeven, Not a Number.

Om de sensor te gebruiken moeten alle files uit de [library folder](../lib/) naar de Raspberrypi Pico gekopieerd worden en daar in de `lib/` folder geplaats worden. Zie hiervoor het hoofdstuk [Thonny](../methode/thonny). 

## Aansluiting
De sensoren (sluit ze niet beide aan op een enkele Raspberry Pi Pico, daarvoor kan de Pico niet genoeg stroom leveren door de pinnen) moeten aangesloten worden volgens het aansluitschema:
 * [SPS30](methode/sps30.md)
 * [SEN63-C](methode/sen63c.md)


