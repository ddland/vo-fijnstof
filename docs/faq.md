# Frequently asked questions (vaak gestelde vragen)

Vaak gestelde vragen, oftwel problemen waarop al een antwoord zou moeten zijn.

## De sensor werkt niet!
Let goed op de aansluiting (de SENC-63C moet op 3.3V aangesloten zijn, pin 36 van de Raspberry Pi Pico), de SP30 moet op 5V worden aangesloten (pin 39 of 40). 

Als alle pinnen goed aangesloten zijn kan het zijn dat de I2C bus corrupt is geraakt door het aansluiten van de sensoren terwijl de Pico nog aangesloten was. Verwijder de USB-kabel, wacht een paar seconden en verbind de sensor opnieuw. 

## De data ziet er gek uit
Let op bij het inlezen van data op het data-format. Er zit standaard een `,` tussen het gehele getal en de decimalen. Standaard in Nederland is dat een `.`. Het software pakket Microsoft Excel kan hier niet goed mee omgaan en het is erg makkelijk om een data-bestand daardoor ongemerkt te veranderen. Maak gebruik van een simpele tekst-verwerker om de `.csv` bestanden te openen. Daarmee kan je zien of de data er redelijk (vergelijkbaar met de data hier) uitziet.

## Ik meet niet veel fijnstof
Je meet een concentratie van een stof waar je buiten niet direct invloed op hebt. Als je lage waarden meet, kan het dus zo zijn dat er weinig fijnstof in de lucht aanwezig is. Om dit te controleren kan je bij sensoren in de buurt kijken. Bijvoorbeeld bij [samenmeten.nl](https://samenmeten.nl/dataportaal) of rond Delft door het [Ohnics](https://ohnics.online) netwerk te bekijken. 
