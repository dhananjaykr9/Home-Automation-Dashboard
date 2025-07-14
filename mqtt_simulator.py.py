import paho.mqtt.client as mqtt
import time
import random
from datetime import datetime

broker = "localhost"
port = 1883
topic = "home/room1/sensors"

client = mqtt.Client()
client.connect(broker, port)

while True:
    temp = round(random.uniform(24.0, 30.0), 2)
    hum = round(random.uniform(40.0, 55.0), 2)

    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")

    payload = {
        "temperature": f"{temp} °C",
        "humidity": f"{hum} %",
        "date": date_str,
        "time": time_str
    }

    import json
    client.publish(topic, json.dumps(payload))
    print("Published:", payload)
    time.sleep(5)
