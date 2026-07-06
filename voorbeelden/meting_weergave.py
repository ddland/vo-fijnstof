import machine
import time

# Importeer de SEN63C of SEN66 bibliotheek
# zet een # voor de regel die je niet nodig hebt!
from meting_sen6x import Sensor            # SEN63-C fijnstof sensor
#from meting_sps30 import SPS30 as Sensor  # SPS30 fijnstof sensor

# maak verbinding met de fijnstof sensor
# sensor verbonden met pin 0 en 1 (sda en scl) op de Raspberrypi Pico.
i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=100000)

delay = 5 # wacht 5 seconden na elke meting
separator = ";" # scheidingsteken tussen de verschillende meetwaarden

#### Geen wijzigingen meer nodig #####

sensor = Sensor(i2c)
sensor.start_measurement()
sensor.meet_data()
time.sleep(1)
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
