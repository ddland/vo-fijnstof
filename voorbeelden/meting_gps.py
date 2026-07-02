import machine
import time
import micropyGPS
import _thread

# Importeer de SEN63C of SEN66 bibliotheek
# zet een # voor de regel die je niet nodig hebt!
from meting_sen6x import SEN

# Importeer de SPS30 bibliotheek
#from meting_sps30 import SPS30 as SEN

delay = 5 # wacht 5 seconden na elke meting

class GPS:
    """ Class om een GPS UART sensor in een andere thread data te laten
        vergaren. Datum wordt in een datetime object beschikbaar gesteld.
    """
    def __init__(self, uart, parser):
        self.uart = uart
        self.parser = parser
        self.running = False
        self._status = None
        self.gpsdata = []
        
    def datetime(self, date, time):
        return '20%d%d%d:%d%d%f' %(date[2],date[1],date[0],time[0],time[1],time[2])
        
    def stop(self):
        self.running = False
        
    def start(self):
        self.running = True
        while self.running:
            if self.uart.any():
                try:
                    data = self.uart.read().decode('utf-8')
                except UnicodeError:
                    continue # could not pass lines of data, skip
                except Exception as e:
                    print(e)
                    continue
                if data:
                    for ii in data:
                        status = self.parser.update(ii)
                if parser.valid:
                    self.gpsdata = [self.datetime(self.parser.date, self.parser.timestamp),
                                    self.parser.latitude, self.parser.longitude, time.time_ns()]
                    
            else:
                time.sleep(0.01)
        

if __name__ == "__main__":
    # GPS op pin 4 en 5 van de Raspberrypi Pico aangesloten
    uart = machine.UART(1, baudrate=9600, tx=machine.Pin(4), rx=machine.Pin(5))
    parser = micropyGPS.MicropyGPS(location_formatting='dd')
    gps = GPS(uart, parser)
    # start GPS op een andere thread, kan hier de fijnstof gemeten worden.
    _thread.start_new_thread(gps.start, ())
    
    delay = 5 # wacht 5 seconden na elke meting
    separator = ";" # scheidings teken tussen de verschillende meetwaarden

    # maak verbinding met de sensor en start de sensor op (duurt ~ 10 seconden)
    # sensor verbonden met pin 0 en 1 (sda en scl) op de Raspberrypi Pico.
    i2c = machine.I2C(0, sda = machine.Pin(0), scl = machine.Pin(1), freq=100000)

    sensor = SEN(i2c)
    sensor.start_measurement()

    # start de metingen
    measure = 1
    while measure:
        try:
            # zolang ctrl-c niet ingedrukt...
            sensor.meet_data()
            data = separator.join(str(ii) for ii in sensor.waarden)
            print(data)
            print(gps.gpsdata)
            time.sleep(delay)
        except KeyboardInterrupt:
            measure = 0
            gps.running = False
    
    while gps.running: # laat de gps afsluiten
        pass
    print('all done...')
    


