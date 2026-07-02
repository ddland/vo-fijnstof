import machine
import time
import struct
# library voor een oled (SSD1306) scherm
import ssd1306

# Importeer de SEN63C of SEN66 bibliotheek
# zet een # voor de regel die je niet nodig hebt!
from meting_sen6x import SEN

# Importeer de SPS30 bibliotheek
#from meting_sps30 import SPS30 as SEN

def write(display, text, x,y):
    """ Geef de text weer op locatie  (x,y).
    Bij meerdere regels text, maak lijsten met text en x,y coordinaten.
    x (0 - 62), y (16 - 64)
    """ 
    display.fill(0) # black
    if isinstance(text, list):
        for ii in range(len(text)):
            display.text(text[ii], x[ii], y[ii])
    else:
        display.text(text,x,y)
    display.show()

delay = 5 # wacht 5 seconden na elke meting

# maak verbinding met het scherm
i2c_oled = machine.I2C(1, sda = machine.Pin(14), scl = machine.Pin(15))

# kies voor een vierkant (64x64) scherm of rechthoekig (128x64) pixels.
#display = ssd1306.SSD1306_I2C(64,64, i2c_oled)
display = ssd1306.SSD1306_I2C(128,64, i2c_oled)

write(display, 'starting', 0,16)

# maak verbinding met de sensor en start de sensor op (duurt ~ 10 seconden)
# sensor verbonden met pin 0 en 1 (sda en scl) op de Raspberrypi Pico.
i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=100000)

sensor = SEN(i2c)
sensor.start_measurement()


# start metingen
measure = 1
t0 = time.time()
while measure:
    try:
        # zolang ctrl-c niet ingedrukt...
        sensor.meet_data()
        data = sensor.waarden
        # schrijf de data weg naar het scherm
        # eerste regel de tijd (sinds het opstarten van de meting)
        # tweede regel PM1.0
        # derde  regel PM2.5
        # vierde regel PM5
        write(display, ['t:%d' %(data[0] - t0), '1.0:%2.2f' %(data[1]), '2.5:%2.2f' %(data[2])], [0,0,0], [16,32,48])
        time.sleep(delay)
    except KeyboardInterrupt:
        measure = 0        
        
        
    
