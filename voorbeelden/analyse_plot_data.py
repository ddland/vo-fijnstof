import numpy as np
import matplotlib.pyplot as plt

# lees data
# 1e rij is de beschrijving
data = np.loadtxt('data/meting_001.csv',
                  delimiter=';',
                  skiprows=1)

# creeer een tijds-as
t = np.asarray(data[:,0], dtype='datetime64[s]')

t = t - t[0] # laat de meting op t=0 seconden beginnen

# maak 3 figuren aan
fig, ax = plt.subplots(3, sharex=True, figsize=(10,15))
ax[0].plot(t, data[:,1], label='PM 1.0')
ax[0].plot(t, data[:,2], label='PM 2.5')
ax[0].plot(t, data[:,3], label='PM 4.0')
ax[0].plot(t, data[:,4], label='PM 10')
ax[1].plot(t, data[:,5], label='Temperatuur')
ax[2].plot(t, data[:,6], label='Rel. Luchtvochtigheid')
# teken grid, assen
ax[0].grid()
ax[1].grid()
ax[2].grid()
plt.xlabel('tijd [s]')
ax[0].set_ylabel('fijnstof [ug/m]')
ax[0].legend(loc=0)
ax[1].set_ylabel('temperatuur [degC]')
ax[1].legend(loc=0)
ax[2].set_ylabel('rel. luchtvochtigheid [%]')
ax[2].legend(loc=0)
plt.gcf().autofmt_xdate()

# sla het figuur op
plt.savefig('analyse_data.jpg')
plt.show()
