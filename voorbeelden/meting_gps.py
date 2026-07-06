import machine
import time
import gps

# Importeer de SEN63C of SEN66 bibliotheek
# zet een # voor de regel die je niet nodig hebt!
from meting_sen6x import Sensor            # SEN63-C fijnstof sensor
#from meting_sps30 import SPS30 as Sensor  # SPS30 fijnstof sensor

# maak verbinding met de fijnstof sensor
# sensor verbonden met pin 0 en 1 (sda en scl) op de Raspberrypi Pico.
i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=100000)

# maak verbinding met de GPS
# GPS op pin 4 en 5 van de Raspberrypi Pico aangesloten
uart = machine.UART(1, baudrate=9600, tx=machine.Pin(4), rx=machine.Pin(5))

delay = 5 # wacht 5 seconden na elke meting
separator = ";" # scheidings teken tussen de verschillende meetwaarden


#### Geen wijzigingen meer nodig #####
gps = gps.GPS(uart)
sensor = Sensor(i2c)
sensor.start_measurement()

# start de metingen
measure = 1
while measure:
    try:
        # zolang ctrl-c niet ingedrukt...
        sensor.meet_data()
        data = separator.join(str(ii) for ii in sensor.waarden)
        print('sensor: ',data)
        print('gps: ',gps.gpsdata)
        time.sleep(delay)
    except KeyboardInterrupt:
        measure = 0
        gps.running = False

while gps.running: # laat de gps afsluiten
    pass
print('all done...')
    


