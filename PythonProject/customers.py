import json

def load_customers(path):
    try:
        f = open(path, 'r')
        data = json.load(f)
        return data
    except:
        return []

def save_customers(path, customers):
    f = open(path, 'w')
    json.dump(customers, f, indent=4)

def register_customer(customers, profile):
    customers.append(profile)
    return profile

def authenticate_customer(customers, license_number, pin):
    for c in customers:
        if c['license_number'] == license_number and str(c['pin']) == str(pin):
            return c
    return None

def update_customer_profile(customers, customer_id, updates):
    for c in customers:
        if c['id'] == customer_id:
            c.update(updates)
            return c
    return {}