from sen6x import SEN6X
import time 

"""
Class voor de SEN62-C
Aansluiting (barcode leesbaar naar je toe gericht):

 -------------------
 |   --   [barcode]|
 |  /  \           |
 |  \  /--------|  |
 |   --  123456 |  |
 -------------------
 Pin layout:
 1: VDD (3.3V)
 2: GND
 3: SCL
 4: SDA
 5: GND
 6: VDD (3.3V)

Er hoeft maar 1 van de twee VDD en GND aansluitingen angesloten te zijn. 
"""

class SEN(SEN6X):
    data_header = ['tijd [s]','pm 1.0 [ug/m3]','pm 2.5 [ug/m3]','pm 4.0 [ug/m3]','pm 10 [ug/m3]', 'temp [degC]', 'rel. hum [%]']
    waarden = [0,0,0,0,0,0,0]
    
    def meet_data(self):
        data = self.get_data()
        self.waarden[0] = time.time()
        self.waarden[1:] = self.last_measurement[:6]
