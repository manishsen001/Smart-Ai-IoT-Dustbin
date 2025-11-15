from sensors.ultrasonic import get_distance
from sensors.weight_sensor import get_weight
from utils.servo import open_lid, close_lid
from ml.classifier import classify
from iot.mqtt_client import send_data
import json
import time

def run_dustbin():
    while True:
        distance = get_distance()

        if distance < 20:   # User detected
            open_lid()
            time.sleep(4)
            close_lid()

        weight = get_weight()
        trash_type = classify([distance, weight])

        data = {
            "distance_cm": distance,
            "weight_g": weight,
            "trash_type": trash_type,
            "timestamp": time.time()
        }

        send_data(json.dumps(data))
        time.sleep(5)