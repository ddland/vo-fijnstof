# Uitwerking

Als de meetdata zijn opgeslagen, ontstaan er bestanden met veel datapunten. Om inzicht te krijgen in de gemeten waarden, moeten deze data op een duidelijke manier worden weergegeven.

Een mogelijkheid is om de gemeten waarden uit te zetten tegen de tijd. Op de x-as (horizontale as) staat dan de tijd. Op de y-as (verticale as) staan bijvoorbeeld de gemeten fijnstofconcentratie, temperatuur en/of relatieve luchtvochtigheid.

```python
import numpy as np
import matplotlib.pyplot as plt

# lees data
data = np.loadtxt('data/03_buiten.csv',
                  delimiter=';',
                  skiprows=1)

# creeer een tijds-as
t = np.asarray(data[:,0], dtype='datetime64[s]')
t = t - t[0] # laat de meting op t=0 beginnen

# plot de eerste column uitgezet tegen de tijd
plt.plot(t, data[:,1], label='PM 1.0')
plt.plot(t, data[:,2], label='PM 2.5')
plt.plot(t, data[:,3], label='PM 4.0')
plt.plot(t, data[:,4], label='PM 10')

# teken grid, assen
plt.grid()
plt.xlabel('tijd [s]')
plt.ylabel('fijnstof [ug/m]')
plt.legend(loc=0)
plt.gcf().autofmt_xdate()

# sla het figuur op
plt.savefig('simple_fig.jpg')
plt.show()
```
