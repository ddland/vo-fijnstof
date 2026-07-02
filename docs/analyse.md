# Uitwerking
Als de data van de metingen opgeslagen is zijn er bestanden met erg veel data punten. Om inzicht te krijgen in de waarden die gemeten zijn moeten deze op een andere manier weergegeven worden. Een van de mogelijkheiden is om de gemeten waarden uit te zetten tegen de tijd. Op de x-as (horizontale as) staat dan de tijd, terwijl op de y-as (vertical as) de gemeten blootstelling, temperatuur en/of relatieve luchtvochtigheid staat. 

``` {code}
from matplotlib import rcParams, cycler
import matplotlib.pyplot as plt
import numpy as np
plt.ion()

# Fixing random state for reproducibility
np.random.seed(19680801)

N = 10
data = [np.logspace(0, 1, 100) + np.random.randn(100) + ii for ii in range(N)]
data = np.array(data).T
cmap = plt.cm.coolwarm
rcParams['axes.prop_cycle'] = cycler(color=cmap(np.linspace(0, 1, N)))


from matplotlib.lines import Line2D
custom_lines = [Line2D([0], [0], color=cmap(0.), lw=4),
                Line2D([0], [0], color=cmap(.5), lw=4),
                Line2D([0], [0], color=cmap(1.), lw=4)]

fig, ax = plt.subplots(figsize=(10, 5))
lines = ax.plot(data)
ax.legend(custom_lines, ['Cold', 'Medium', 'Hot']);
```
