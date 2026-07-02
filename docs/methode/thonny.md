# Thonny

Een relatief makkelijke editor om te werken met de Raspberrypi Pico is [Thonny](https://thonny.org). Deze editor maakt het mogelijk om code op de Raspberrypi Pico uit te voeren, maar ook om bestanden aan te maken die later uitgevoerd moeten worden. Daarnaast is het mogelijk om data van de Raspberrpyi Pico te downloaden als een meting is uitgevoerd.

Na installatie van Thonny kan je kiezen in welke taal het programma weergeven moet worden. 
```{image} ../../images/thonny_0.png
:alt: Eerste pop-up van Thonny om aan te geven in welke taal je de software wilt gebruiken. 
:width: 50%
:align: center
```
Waarna een `<untitled>` of `<naamloos>` document geopend wordt in het bovenste scherm, de `editor`. Met de `shell` weergegeven in het onderste scherm. 
```{image} ../../images/thonny_1.png
:alt: Eerste keer opstarten van Thonny met een leeg scherm in het bovenste deel, de Shell in het onderste deel van het scherm.
:width: 50%
:align: center
``` 

In het `editor` scherm kan je de code schrijven die je wilt uitvoeren. Hier kunnen ook meerdere tabs geopend worden om zo tegelijkertijd meerdere bestanden te kunnen bewerken. 
In het `shell` scherm is the Python prompt `>>>` zichtbaar. Wat je hier typt wordt gelijk uitgevoerd (geinterpreteerd) door Python en de resultaten worden op de regel(s) daaronder weergeven. Door bijvoorbeeld `6 * 7` na de prompt in te typen kan je het antwoord op [alles](https://en.wikipedia.org/wiki/Phrases_from_The_Hitchhiker%27s_Guide_to_the_Galaxy#The_Answer_to_the_Ultimate_Question_of_Life,_the_Universe,_and_Everything_is_42) terug krijgen.
```{image} ../../images/thonny_3.png
:alt: Een eerste bereking in de shell van Thonny met als antwoord 42.
:width: 50%
:align: center
```

Onderin het scherm staat `Local Python` met een naam van een uitvoerbaar bestand. Dit is de Python versie die nu gebruikt wordt om de berekeningen uit te voeren. Door op de text `Local Python` te klikken open je een menu waar je een andere versie van Python kan selecteren. Als een Raspberrypi Pico is aangesloten krijg je die dan ook te zien. 
:::{image} ../../images/thonny_4.png
:alt: Keuze tussen de verschillende Python versies, op de Raspberrypi Pico of een lokale versie.
:width: 50%
:align: center
:::

Door in het `view` of `weergave` menu de optie `files` of `bestanden` aan te vinken worden de bestanden op de computer (`This computer`) en als een Raspberrypi Pico is aangesloten op de Pi (`Raspberry Pi Pico`) weergegeven. Klikken op de 3 horizontale lijnen aan de rechterkant van het `Files` of `Bestanden` venster opent een pop-up menu om bestanden tussen de computer en Raspberrypi te verplaatsen en te beheren.

::::{grid} 2
:gutter: 3
:::{image} ../../images/thonny_5.png
:width: 100%
:::

:::{image} ../../images/thonny_6.png
:width: 100%
:::

::::

Rechtsklikken op een bestand of folder opent ook een pop-up menu voor het, op een makkelijke manier, verplaatsen van bestanden tussen de Raspberrypi en de computer. 

## Micropython
Als je met de Raspberrypi Pico aan de slag gaat moet Thonny de code uitvoeren met de Python versie die draait op de Raspberrypi Pico. Deze versie is een micro-python distributie. De code lijkt erg veel op standaard python, maar er zijn andere bibliotheken beschikbaar en veel standaard bibliotheken zijn niet aanwezig. De microcontroller heeft zelf geen weergave mogelijkheden, dus is het ook niet noodzakelijk om software mee te leveren waarmee een figuur weergegeven kan worden. Aan de andere kant zijn er wel mogelijkheden om hardware aan te sluiten, dus daar zijn wel de bibliotheken voor aanwezig.


