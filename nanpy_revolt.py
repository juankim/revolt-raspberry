from nanpy import (ArduinoApi, SerialManager, OneWire)

connection = SerialManager(device='/dev/ttyACM0')
connection.baudrate=9600
#a = ArduinoApi(connection=connection)
#a.pinMode(13, a.OUTPUT)
#a.digitalWrite(13,a.HIGH)

connection.write("5")
