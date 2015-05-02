import os
import json

sensorsJSON = open(os.path.dirname(os.path.realpath(__file__)) + "/sensors.json", 'r')
sensors = json.loads(sensorsJSON.read())

id = '0101'
type = 'temperature'

for item in sensors:
    if sensors[item]['ID'] == id and sensors[item]['description'] == type:
    	my_item = item
       	break
else:
    my_item = None


print my_item

