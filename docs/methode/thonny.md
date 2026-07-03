# Thonny

Een relatief eenvoudige editor om met de Raspberry Pi Pico te werken is [Thonny](https://thonny.org). Met deze editor kun je code op de Raspberry Pi Pico uitvoeren. Je kunt ook bestanden aanmaken die later uitgevoerd moeten worden. Daarnaast kun je data van de Raspberry Pi Pico downloaden nadat een meting is uitgevoerd.

Na de installatie van Thonny kun je kiezen in welke taal het programma moet worden weergegeven.

```{image} ../../images/thonny_0.png
:alt: Eerste pop-up van Thonny om aan te geven in welke taal je de software wilt gebruiken.
:width: 50%
:align: center
```

Daarna wordt een `<untitled>`- of `<naamloos>`-document geopend in het bovenste scherm: de `editor`. De `shell` staat in het onderste scherm.

```{image} ../../images/thonny_1.png
:alt: Eerste keer opstarten van Thonny met een leeg scherm in het bovenste deel, de Shell in het onderste deel van het scherm.
:width: 50%
:align: center
```

In het `editor`-scherm kun je de code schrijven die je wilt uitvoeren. Je kunt ook meerdere tabs openen, zodat je meerdere bestanden tegelijk kunt bewerken.

In het `shell`-scherm is de Python-prompt `>>>` zichtbaar. Wat je hier typt, wordt meteen uitgevoerd door Python. De resultaten verschijnen op de regels daaronder. Als je bijvoorbeeld `6 * 7` na de prompt typt, krijg je het antwoord op [alles](https://en.wikipedia.org/wiki/Phrases_from_The_Hitchhiker%27s_Guide_to_the_Galaxy#The_Answer_to_the_Ultimate_Question_of_Life,_the_Universe,_and_Everything_is_42) terug.

```{image} ../../images/thonny_3.png
:alt: Een eerste berekening in de shell van Thonny met als antwoord 42.
:width: 50%
:align: center
```

Onderin het scherm staat `Local Python` met de naam van een uitvoerbaar bestand. Dit is de Python-versie die op dat moment wordt gebruikt om de berekeningen uit te voeren. Door op de tekst `Local Python` te klikken, open je een menu waarin je een andere versie van Python kunt selecteren. Als een Raspberry Pi Pico is aangesloten, krijg je die daar ook te zien.

:::{image} ../../images/thonny_4.png
:alt: Keuze tussen de verschillende Python-versies, op de Raspberry Pi Pico of een lokale versie.
:width: 50%
:align: center
:::

Door de MicroPython versie op de Raspberry Pi Pico te selecteren gebruik je de Python versie die op de micro-controller draait. Hier heb je dan de mogelijkheid om de hardware aan te sturen.

Door in het menu `view` of `weergave` de optie `files` of `bestanden` aan te vinken, worden de bestanden zichtbaar. Je ziet dan de bestanden op de computer (`This computer`) en, als een Raspberry Pi Pico is aangesloten, ook de bestanden op de Pico (`Raspberry Pi Pico`). Klik op de drie horizontale lijnen aan de rechterkant van het `Files`- of `Bestanden`-venster om een pop-upmenu te openen. Daarmee kun je bestanden tussen de computer en de Raspberry Pi Pico verplaatsen en beheren.

::::{grid} 2
:gutter: 3
:::{image} ../../images/thonny_5.png
:width: 100%
:::

:::{image} ../../images/thonny_6.png
:width: 100%
:::

::::

Met de rechtermuisknop klikken op een bestand of map opent ook een pop-upmenu. Daarmee kun je op een makkelijke manier bestanden verplaatsen tussen de Raspberry Pi Pico en de computer. Zo kan je door rechts te klikken op de 'lib' folder in het `This computer` scherm, in 1 keer de hele folder naar de Raspberry Pi Pico kopieren.

## Python Libraries

Voor python zijn veel modules beschikbaar die het makkelijk maken om met data te werken, grafieken weer te geven en wetenschappelijke berekeninge uit te voeren. Deze modules kan je vanuit Thonny installeren. 
Om de modules te installeren moet je op de `Local Python` werken, controleer dit in de informatie balk rechts onderin het scherm. 

:::{image} ../../images/thonny_7.png
:width: 100%
:::

Door in het pop-scherm `matplotlib`, `numpy` en `pandas` te installeren kan je daarna gebruik maken van deze modules.


# MicroPython

Als je met de Raspberry Pi Pico aan de slag gaat, moet Thonny de code uitvoeren met de Python-versie die op de Raspberry Pi Pico draait. Deze versie heet MicroPython. De code lijkt veel op gewone Python, maar er zijn andere bibliotheken beschikbaar. Veel standaardbibliotheken zijn niet aanwezig.

De microcontroller heeft zelf geen scherm. Daarom is het niet nodig om software mee te leveren waarmee figuren kunnen worden weergegeven. Er zijn wel mogelijkheden om hardware aan te sluiten. Voor die hardware zijn vaak speciale bibliotheken beschikbaar.

## Automatisch uitvoeren
Om een bestand automatisch uit te voeren (je hebt dan geen computer meer nodig om een script uit te voeren) moet de naam van het bestand `main.py` zijn. Ook moet het bestand in de root directory van de Raspberry Pi Pico opgeslagen zijn. 

Door onderstaande code in het bestand main.py te zetten gaat de groene LED van de Raspberry Pi Pico 5 keer knipperen zodra de Raspberry Pi Pico van stroom voorzien wordt (vanaf de micro-usb kabel verbonden met de computer, of via een powerbank). 

```python
import machine
import time

led = machine.Pin('LED', machine.Pin.OUT)

for ii in range(5):
    led.toggle()
    time.sleep(1)
```


