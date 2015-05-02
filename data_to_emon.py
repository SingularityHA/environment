"""
    SingularityHA Environment
    ~~~~~~~~~~~~~~~~~~~~~~~~

    :copyright: (c) 2013- by Internet by Design Ltd
    :license: GPL v3, see LICENSE for more details.

"""
import mosquitto
import json
import time
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir)) + "/../lib")
from config import config
import logging
import requests

sensorsJSON = open(os.path.dirname(os.path.realpath(__file__)) + "/sensors.json", 'r')
sensors = json.loads(sensorsJSON.read())

logger = logging.getLogger("environment.emonsender")

broker = str(config.get("mqtt", "host"))
port = int(config.get("mqtt", "port"))

mqttc = mosquitto.Mosquitto("singularity-environment-emonsender")

emonhost = config.get("environment", "emonhost")
emon_api_key = config.get("environment", "apikey")

def on_message(mosq, obj, msg):
    inbound = json.loads(msg.payload)

    deviceID = inbound['deviceID']
    data = inbound['data']
    description = inbound['description']

    for item in sensors:
        if sensors[item]['ID'] == deviceID and sensors[item]['description'] == description:
       	    current_item = item
       	    break
    else:
        current_item = None

    if description == "temperature":
	data = str(data)+"c"
	
    if description == "humidity":
	data = str(data)+"%"

	logger.debug("Attempting to send data")
    r = requests.get("http://"+emonhost+"/emoncms/input/post.json?json={"+str(current_item)+":"+data+"}&apikey="+emon_api_key)
    if r.content == "ok":
	logger.debug("Sent data OK")


def main():
    try:
	logger.info("Starting...")
        mqttc.on_message = on_message

        mqttc.connect(broker, port, 60, False)

        mqttc.subscribe("environment", 0)
	logger.info("Started.")
        while mqttc.loop() == 0:
            pass
    except KeyboardInterrupt:
        pass
