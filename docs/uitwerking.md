# Uitwerking

Als de meetdata zijn opgeslagen, ontstaan er bestanden met veel datapunten. Om inzicht te krijgen in de gemeten waarden, moeten deze data op een duidelijke manier worden weergegeven.

## Thonny

Belanrijk in Thonny is er op te letten welke Python versie je gebruikt. Voor de analyse van de data is geen microcontroller nodig, maar juist een scherm. Micro-python is hier dus niet geschikt. Let er op dat rechts onderin Thonny nu de 'Local Python' interpreter gekozen is.


## Metingen uitgezet tegen de tijd
Een mogelijkheid is om de gemeten waarden uit te zetten tegen de tijd. Op de x-as (horizontale as) staat dan de tijd. Op de y-as (verticale as) staan bijvoorbeeld de gemeten fijnstofconcentratie, temperatuur en/of relatieve luchtvochtigheid.
In het voorbeeld figuur worden er 3 figuren aangemaakt, elk met dezelfde tijds-as. Hierdoor is het makkelijk om verschillende variabelen met elkaar op hetzelfde tijdstip te vergelijken. 

``` {literalinclude} ../voorbeelden/analyse_plot_data.py
```
De grafiek ziet er dan zo uit:
```{image} ../images/analyse_data.jpg
:width: 70%
:align: center
```

Door zo van elke meting een grafiek te maken kan je verschillen bestuderen. Is een meting op een ander moment (of locatie) heel anders? Zijn de omstandigheden (temperatuur, luchtvochtigheid) voor beide meetseries gelijk? 

## Metingen vergelijken
Door verschillende metingen uitgezet tegen de tijd met elkaar te vergelijken kan je proberen patronen te herkennen. Is een meting tijdens de avond-spits langs een drukke weg echt anders dan een meting op een rustig moment? Of geven de klaslokalen tijdens een tussen-uur een lagere concentratie fijnstof dan tijdens een druk bezette les? Maar het is moeilijk om de lijnen met elkaar te vergelijken. 

Een andere methode is om de totale meting als input te gebruiken. Door het gemiddelde te bereken van alle meetpunten kan je direct metingen vergelijken. Om het gemiddelde van een dataset te berekenen kan je alle datapunten bij elkaar optellen en daarna delen door het aantal datapunten:
```python
data  = [1,2,3,4,5,6,7,9,10]
gem = 0
for getal in data:
   gem = gem + data # voeg een nieuwe waarden toe aan het gemiddelde

gem = gem / len(data) # deel door het aantal opgetelde elementen
print(gem) # geef de waarde weer
```

Op deze manier kan je in de conclusies van je onderzoek enkele getallen met elkaar vergelijken. 

### Boxplot
Grafisch is het mogelijk om een box-plot te maken. Hierbij laat je niet alleen het gemiddelde zien, maar ook hoe de verdeling van de datapunten rond dat gemiddelde plaats vindt. Door je dataset zo vorm te geven dat elke afzonderlinge meting (bijvoorbeeld een route op de fiets en met de brommer, metingen op maandag en woensdag, metingen in een vol lokaal en een leeg lokaal of metingen thuis en op school) als een individuele data-file opgeslagen is kan je met de volgende voorbeeldcode de data weergeven:

``` {literalinclude} ../voorbeelden/analyse_boxplot.py
```
De grafiek ziet er dan zo uit:
```{image} ../images/boxplot.jpg
:width: 70%
:align: center
```

In een oogopslag is duidelijk of er wel of geen verschillen zijn tussen de verschillende meetseries. Door in de code extra datasets toe te voegen (een extra file in de directory `data` plaatsen is al voldoende) kan je zo meerdere `boxen` naast elkaar krijgen. Kies wel voor een duidelijke beschrijving van de verschillende `boxen`. Meting 1 en 2 zegt niet zoveel voor de lezer. Als daar 'Thuis' en 'School' had gestaan was het al veel duidelijker geweest wat er gemeten is. 

