import network
import socket

# Importeer de SEN63C of SEN66 bibliotheek
# zet een # voor de regel die je niet nodig hebt!
from meting_sen6x import Sensor            # SEN63-C fijnstof sensor
#from meting_sps30 import SPS30 as Sensor  # SPS30 fijnstof sensor

# maak verbinding met de fijnstof sensor
# sensor verbonden met pin 0 en 1 (sda en scl) op de Raspberrypi Pico.
i2c = machine.I2C(1, sda = machine.Pin(2), scl = machine.Pin(3), freq=100000)
sensor = Sensor(i2c)
sensor.start_measurement()


## Configureer het accesspoint
# verbind en daarna kan je naar 192.168.4.1 om een meting uit te voeren
ssid = 'vo-fijnstof'
password = '123456789'

ap = network.WLAN(network.AP_IF)
ap.config(essid=ssid, password=password)
ap.active(True)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)

## templates voor de website met en zonder data

webpage_start =  """
<!DOCTYPE HTML>
<html><head>SPS30 measurements</head>
<body><html>
<h2>measured values</h2>
<p>No data yet</p>
<form action="./measure">
<input type ="submit" value="measure" />
</form>
"""

webpage_data = """
<!DOCTYPE HTML>
<html><head>
<title>SPS30 measurements</title>
<style>
table, th, td {border: 1px solid black; border-collapse: collapse;}
th {text-align: left;}
</style>
</head>
<body>
<h2>measured values</h2>
<table >
 <tr >
       <th>tijd [s]</th>
      <th>PM1.0 mg/m^3</th>
      <th>PM2.5 mg/m^3</th>
      <th>PM4.0 mg/m^3</th>
      <th>PM 10 mg/m^3</th>
 </tr>
 <tr>
      <td> %d </td>
      <td> %2.2f </td>
      <td> %2.2f </td>
      <td> %2.2f </td>
      <td> %2.2f </td>
 </tr>
</table>
<form action="./measure">
<input type ="submit" value="measure" />
</form>
</body>
</html>
"""

## start de hoofd-loop, waarin webserver en data uitgelezen worden

run = True
while run:
    try:
        conn, addr = s.accept()
        request = conn.recv(1024).decode('utf-8').lower()
        if request.find('get /measure?') >= 0:
            sensor.meet_data()
            html = webpage_data %tuple(sensor.waarden[:5])
        else:
            html = webpage_start
        conn.send(html)
        conn.close()
    except KeyboardInterrupt as e:
        run = False
s.close()
