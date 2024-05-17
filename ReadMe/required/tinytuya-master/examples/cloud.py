# TinyTuya Example
# -*- coding: utf-8 -*-
"""
 TinyTuya - Tuya Cloud Functions

 This examples uses the Tinytuya Cloud class and functions
 to access the Tuya Cloud to pull device information and
 control the device via the cloud.

 Author: Jason A. Cox
 For more information see https://github.com/jasonacox/tinytuya

""" 
import tinytuya

# Turn on Debug Mode
tinytuya.set_debug(True)

# You can have tinytuya pull the API credentials
# from the tinytuya.json file created by the wizard
# c = tinytuya.Cloud()
# Alternatively you can specify those values here:
# Connect to Tuya Cloud
c = tinytuya.Cloud(
        apiRegion="us", 
        apiKey="xxxxxxxxxxxxxxxxxxxx", 
        apiSecret="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", 
        apiDeviceID="xxxxxxxxxxxxxxxxxxID")

# Display list of devices
devices = c.getdevices()
print("Device List: %r" % devices)

# Select a Device ID to Test
id = "xxxxxxxxxxxxxxxxxxID"

# Display Properties of Device
result = c.getproperties(id)
print("Properties of device:\n", result)

# Display Functions of Device
result = c.getfunctions(id)
print("Functions of device:\n", result)

# Display DPS IDs of Device
result = c.getdps(id)
print("DPS IDs of device:\n", result)

# Display Status of Device
result = c.getstatus(id)
print("Status of device:\n", result)

# Send Command - This example assumes a basic switch
commands = {
	'commands': [{
		'code': 'switch_1',
		'value': True
	}, {
		'code': 'countdown_1',
		'value': 0
	}]
}
print("Sending command...")
result = c.sendcommand(id,commands)
print("Results\n:", result)

# Get device logs
# Note: the returned timestamps are unixtime*1000
# event_id 7 (data report) will probably be the most useful
# More information can be found at https://developer.tuya.com/en/docs/cloud/cbea13f274?id=Kalmcohrembze

# Get device logs from the last day
result = c.getdevicelog(id)
print("Device logs:\n", result)

# Get device logs from 7 days ago through 5 days ago (2 days worth)
#result = c.getdevicelog(id, start=-7, end=-5)
#print("Device logs:\n", result)

# Get device logs for one day ending an hour ago
#result = c.getdevicelog(id, end=time.time() - 3600)
#print("Device logs:\n", result)
