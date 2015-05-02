import os
import json

sensorsJSON = open(os.path.dirname(os.path.realpath(__file__)) + "/sensors.json", 'r')
sensors = json.loads(sensorsJSON.read())

print sensors

