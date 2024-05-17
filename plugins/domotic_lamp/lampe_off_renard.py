import tinytuya
import time

# Remplacez 'DEVICE_ID', 'IP_ADDRESS' et 'LOCAL_KEY' par les valeurs appropriées
DEVICE_ID = 'bf410f2735249b01f4pnpo'
IP_ADDRESS = '192.168.129.35'
LOCAL_KEY = "p}eXt:#T/4X'sci5"


# Connect to Tuya BulbDevice
print('\nConnecting to Tuya Bulb')
d = tinytuya.BulbDevice(DEVICE_ID, IP_ADDRESS, LOCAL_KEY)
d.set_version(3.3)

# Show status of device
data = d.status()
print('\nCurrent Status of Bulb: %r' % data)

# Check to see if the bulb is on and get state of device
data = d.state()
print('\nStatus of Bulb: %r and the Bulb is: ' % data)
if (data['is_on']==True):
    print('ON')
else:
    print('OFF')

# Power Control Test
print('\nPower Control Test')
print('    Turn off lamp')
d.turn_off()
