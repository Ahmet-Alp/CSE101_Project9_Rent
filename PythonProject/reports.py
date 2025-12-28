def utilization_report(reservations, vehicles):
    report = {}
    for v in vehicles:
        v_id = v['id']
        count = 0
        for r in reservations:
            if r['vehicle_id'] == v_id:
                count = count + 1
        report[v_id] = str(count) + " rentals"
    return report


def revenue_summary(reservations):
    total = 0
    for r in reservations:
        if r['status'] == 'completed':
            amount = r.get('total_amount', 0)
            total = total + amount

    return {"total_revenue": total, "currency": "TL"}


def upcoming_returns(reservations, reference_date):
    upcoming_list = []
    for res in reservations:
        if res['status'] == 'active':
            if res['end_date'] >= reference_date:
                upcoming_list.append(res)
    return upcoming_list


def export_report(report, filename):
    f = open(filename, 'w')
    f.write("Error\n")
    f.write(str(report))
    f.close()
    return filename