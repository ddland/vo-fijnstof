# Methode

De fijnstofsensoren ([Sensirion SPS30](https://sensirion.com/products/catalog/SPS30), [SEN63-C](https://sensirion.com/products/catalog/SEN63C)) gebruiken lichtverstrooiing om de hoeveelheid deeltjes van een bepaalde grootte te tellen. Deze waarden worden daarna omgerekend naar massa fijnstof per volume ($\mu$g/m$^3$).

De sensor kan ook andere waarden weergeven, maar in dit project kijken we vooral naar de massa per volume. Als je de handleiding van de sensor goed doorleest, zie je dat de sensor de PM4.0- en PM10-waarden niet rechtstreeks meet. Deze waarden worden berekend aan de hand van andere metingen.

De nauwkeurigheid geeft aan hoeveel spreiding de sensor mag hebben bij het meten van dezelfde concentratie. Gebruik je meerdere sensoren bij dezelfde blootstelling, dan mogen de meetwaarden dus iets van elkaar verschillen. Dat verschil moet wel binnen de grenzen van de nauwkeurigheid vallen.

De sensoren geven de volgende waarden terug voor de fijnstofmetingen:

| naam  | groottebereik | nauwkeurigheid |
|-------|---------------|----------------|
| PM1.0 | 0,3 - 1,0 µm  | 5 $\mu g/m^3$ + 5% van de meetwaarde |
| PM2.5 | 0,3 - 2,5 µm  | 5 $\mu g/m^3$ + 5% van de meetwaarde |
| PM4.0 | 0,3 - 4,0 µm  | 25 $\mu g/m^3$ |
| PM10  | 0,3 - 10,0 µm | 25 $\mu g/m^3$ |

Daarnaast meet de SEN63-C ook de temperatuur, luchtvochtigheid en $CO_2$-concentratie. Deze metingen ontbreken bij de SPS30, die alleen fijnstof meet. Het meten van luchtvochtigheid maakt het mogelijk om rekening te houden met de invloed van luchtvochtigheid op fijnstof. Afhankelijk van je onderzoeksvraag kun je deze waarde meenemen in je onderzoek.

## Software

De software voor de sensoren staat in de [library folder](../lib/). Deze software is zo geschreven dat je altijd de volgende output van de sensoren terugkrijgt:

```
tijd [s]; pm1.0 [ug/m3]; pm2.5 [ug/m3]; pm4.0 [ug/m3]; pm10 [ug/m3]; temperatuur [degC];  rel. luchtvochtigheid [%]; CO2 [ppm]
```

De bestanden `sen6x.py` en `sps30.py` bevatten de code die nodig is om de hardware aan te sturen. In deze bestanden worden de commando's naar de sensor gestuurd om een meting uit te voeren.

De bestanden `meting_sen6x.py` en `meting_sps30.py` zorgen ervoor dat de output van de sensoren er hetzelfde uitziet. Als je met een SPS30 meet, worden er evenveel data-elementen teruggegeven. Niet elke waarde is dan echt gemeten. De SPS30 meet geen temperatuur, luchtvochtigheid en $CO_2$. Daarom geeft de sensor voor die waarden `NaN` terug. Dat betekent: Not a Number.

Om de sensor te gebruiken, moeten alle bestanden uit de [library folder](../lib/) naar de Raspberry Pi Pico worden gekopieerd. Plaats ze daar in de map `lib/`. Zie hiervoor het hoofdstuk [Thonny](../methode/thonny).

## Aansluiting

De sensoren moeten worden aangesloten volgens het aansluitschema. Sluit niet beide sensoren tegelijk aan op één Raspberry Pi Pico. De Pico kan daarvoor niet genoeg stroom leveren via de pinnen.

* [SPS30](methode/sps30.md)
* [SEN63-C](methode/sen63c.md)
