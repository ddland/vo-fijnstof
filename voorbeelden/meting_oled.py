import machine
import time
import ssd1306

# Importeer de SEN63C of SEN66 bibliotheek
# zet een # voor de regel die je niet nodig hebt!
from meting_sen6x import Sensor            # SEN63-C fijnstof sensor
#from meting_sps30 import SPS30 as Sensor  # SPS30 fijnstof sensor

# maak verbinding met de fijnstof sensor
# sensor verbonden met pin 0 en 1 (sda en scl) op de Raspberrypi Pico.
i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=100000)
# scherm verbonden met pin 6 en 7 (sda en scl) op de Raspberrypi Pico
i2c_oled = machine.I2C(1, sda = machine.Pin(6), scl = machine.Pin(7))
# kies voor een vierkant (64x64) scherm of rechthoekig (128x64) pixels.
#display = ssd1306.SSD1306_I2C(64,64, i2c_oled)
display = ssd1306.SSD1306_I2C(128,64, i2c_oled)


delay = 5 # wacht 5 seconden na elke meting
separator = ";" # scheidings teken tussen de verschillende meetwaarden

#### Geen wijzigingen meer nodig #####
ssd1306.write(display, 'starting', 0,16)

sensor = Sensor(i2c)
sensor.start_measurement()

# start metingen
measure = 1
t0 = time.time()
while measure:
    try:
        # zolang ctrl-c niet ingedrukt...
        sensor.meet_data()
        data = sensor.waarden
        print(data)
        # schrijf de data weg naar het scherm
        # eerste regel de tijd (sinds het opstarten van de meting)
        # tweede regel PM1.0
        # derde  regel PM2.5
        # vierde regel PM5
        ssd1306.write(display, ['t:%d' %(data[0] - t0), '1.0:%2.2f' %(data[1]), '2.5:%2.2f' %(data[2])], [0,0,0], [16,32,48])
        time.sleep(delay)
    except KeyboardInterrupt:
        measure = 0        
        
        
    
