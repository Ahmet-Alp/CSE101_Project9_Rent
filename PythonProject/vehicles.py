import json

def load_vehicles(path):
    try:
        f = open(path, 'r')
        data = json.load(f)
        return data
    except:
        return []

def save_vehicles(path, vehicles):
    f = open(path, 'w')
    json.dump(vehicles, f, indent=4)

def add_vehicle(vehicles, vehicle_data):
    vehicles.append(vehicle_data)
    return vehicle_data

def update_vehicle(vehicles, vehicle_id, updates):
    for v in vehicles:
        if v['id'] == vehicle_id:
            v.update(updates)
            return v
    return {}

def set_vehicle_status(vehicles, vehicle_id, status):
    for v in vehicles:
        if v['id'] == vehicle_id:
            v['status'] = status
            return v
    return {}


def list_available_vehicles(vehicles, rental_dates, vehicle_type=None):
    available_list = []
    start_req = rental_dates[0]
    end_req = rental_dates[1]

    for v in vehicles:
        if v['status'] == 'available':
            if vehicle_type == None or v['type'] == vehicle_type:
                if start_req != "" and end_req != "":
                    available_list.append(v)
    return available_list