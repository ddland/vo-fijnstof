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


