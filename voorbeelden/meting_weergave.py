import machine
import time

# Importeer de SEN63C of SEN66 bibliotheek
# zet een # voor de regel die je niet nodig hebt!
from meting_sen6x import SEN

# Importeer de SPS30 bibliotheek
#from meting_sps30 import SPS30 as SEN

delay = 5 # wacht 5 seconden na elke meting
separator = ";" # scheidings teken tussen de verschillende meetwaarden

# maak verbinding met de sensor en start de sensor op (duurt ~ 10 seconden)
# sensor verbonden met pin 0 en 1 (sda en scl) op de Raspberrypi Pico.
i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=100000)

sensor = SEN(i2c)
sensor.start_measurement()

# print de beschrijving van de dataset
print(separator.join(str(ii) for ii in sensor.data_header))

# start de metingen
measure = 1
while measure:
    try:
        # zolang ctrl-c niet ingedrukt...
        sensor.meet_data()
        data = separator.join(str(ii) for ii in sensor.waarden)
        print(data)
        time.sleep(delay)
    except KeyboardInterrupt:
        measure = 0
