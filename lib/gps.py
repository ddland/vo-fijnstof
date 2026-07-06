import micropyGPS
import _thread
import time

class GPS:
    """ Class om een GPS UART sensor in een andere thread data te laten
        vergaren. Datum wordt in een datetime object beschikbaar gesteld.
    """
    def __init__(self, uart):
        self.uart = uart
        self.parser =  micropyGPS.MicropyGPS(location_formatting='dd')
        self.running = False
        self._status = None
        self.gpsdata = []
        _thread.start_new_thread(self.start, ())
        
    def datetime(self, date, time):
        return '20%02d%02d%02d:%02d%02d%05.2f' %(date[2],date[1],date[0],time[0],time[1],time[2])
        
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
                if self.parser.valid:
                    self.gpsdata = [self.datetime(self.parser.date, self.parser.timestamp),
                                    self.parser.latitude[0], self.parser.latitude[1],
                                    self.parser.longitude[0], self.parser.latitude[1],
                                    time.time_ns()]
                    
            else:
                time.sleep(0.01)
        
