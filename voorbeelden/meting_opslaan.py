import machine
import time

# Importeer de SEN63C of SEN66 bibliotheek
# zet een # voor de regel die je niet nodig hebt!
from meting_sen6x import SEN

# Importeer de SPS30 bibliotheek
#from meting_sps30 import SPS30 as SEN

delay = 5 # wacht 5 seconden na elke meting
separator = ";" # scheidings teken tussen de verschillende meetwaarden
basis_fn = 'meting_%03d.csv' # filenaam in de form meting_000.csv
# Als de file al bestaat maakt het script automatisch de volgende aan.

# maak verbinding met de sensor en start de sensor op (duurt ~ 10 seconden)
# sensor verbonden met pin 0 en 1 (sda en scl) op de Raspberrypi Pico.
i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=100000)

sensor = SEN(i2c)
sensor.start_measurement()

# vind de eerste filenaam die nog niet bestaat
N = 0
running = True
while running:
    try:
        fn = basis_fn %(N) 
        vals = os.stat(fn)
        N+=1
    except OSError:
        running = False

# open een lege file
fh = open(fn, 'w')


# print de beschrijving van de dataset naar de file
print(separator.join(str(ii) for ii in sensor.data_header), file=fh)

# start de metingen
measure = 1
while measure:
    try:
        # zolang ctrl-c niet ingedrukt...
        sensor.meet_data()
        data = separator.join(str(ii) for ii in sensor.waarden)
        print(data, file=fh)
        fh.flush() # schrijf de data echt weg naar de file
        time.sleep(delay)
    except KeyboardInterrupt:
        measure = 0
# sluit de file af
fh.close()
