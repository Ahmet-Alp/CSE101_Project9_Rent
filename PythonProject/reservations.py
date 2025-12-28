from datetime import datetime

def check_availability(reservations, vehicle_id, start_date, end_date):
    new_start_date = datetime.strptime(start_date, "%Y-%m-%d")
    new_end_date = datetime.strptime(end_date, "%Y-%m-%d")

    for res in reservations:
        if res['vehicle_id'] == vehicle_id and res['status'] != 'cancelled':
            old_start = datetime.strptime(res['start_date'], "%Y-%m-%d")
            old_end = datetime.strptime(res['end_date'], "%Y-%m-%d")

            if new_start_date < old_end and new_end_date > old_start:
                return False
    return True


def create_reservation(reservations, reservation_data):
    vehicle_id = reservation_data['vehicle_id']
    start_date = reservation_data['start_date']
    end_date = reservation_data['end_date']

    if check_availability(reservations, vehicle_id, start_date, end_date):
        reservations.append(reservation_data)
        return reservation_data
    else:
        return {}


def cancel_reservation(reservations, reservation_id):
    for x in reservations:
        if x['id'] == reservation_id:
            x['status'] = 'cancelled'
            return True
    return False


def complete_rental(reservations, reservation_id, return_data, vehicles):
    for res in reservations:
        if res['id'] == reservation_id:
            res['status'] = 'completed'
            res.update(return_data)

            for veh in vehicles:
                if veh['id'] == res['vehicle_id']:
                    veh['status'] = 'available'
                    if 'mileage' in return_data:
                        veh['mileage'] = return_data['mileage']
            return res
    return {}


def calculate_invoice(reservation, pricing_rules):
    start_date = datetime.strptime(reservation['start_date'], "%Y-%m-%d")
    end_date = datetime.strptime(reservation['end_date'], "%Y-%m-%d")

    days = (end_date - start_date).days
    if days <= 0:
        days = 1

    rate = pricing_rules.get('rate_per_day', 500)
    base_total = days * rate

    tax = base_total * 0.20

    return {
        "days": days,
        "base": base_total,
        "tax": tax,
        "total": base_total + tax
    }