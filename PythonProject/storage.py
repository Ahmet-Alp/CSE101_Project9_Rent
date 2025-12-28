import json
import os
import shutil
from datetime import datetime

def load_state(base_dir):
    files = ["vehicles.json", "customers.json", "reservations.json"]
    results = []

    for f_name in files:
        path = os.path.join(base_dir, f_name)
        try:
            f = open(path, 'r', encoding='utf-8')
            data = json.load(f)
            results.append(data)
        except:
            results.append([])

    return results[0], results[1], results[2]


def save_state(base_dir, vehicles, customers, reservations):
    data_list = [
        ("vehicles.json", vehicles),
        ("customers.json", customers),
        ("reservations.json", reservations)
    ]

    for f_name, content in data_list:
        path = os.path.join(base_dir, f_name)
        f = open(path, 'w', encoding='utf-8')
        json.dump(content, f, indent=4)


def backup_state(base_dir, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)

    now = datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")

    files = ["vehicles.json", "customers.json", "reservations.json"]
    for f in files:
        src = os.path.join(base_dir, f)
        if os.path.exists(src):
            dst = os.path.join(backup_dir, timestamp + "_" + f)
            shutil.copy2(src, dst)
    return []


def validate_reservation(reservation):
    required_fields = ["id", "customer_id", "vehicle_id", "start_date", "end_date"]
    for field in required_fields:
        if field not in reservation:
            return False
    return True