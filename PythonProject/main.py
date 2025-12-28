from storage import load_state, save_state, backup_state
from vehicles import add_vehicle
from customers import register_customer, authenticate_customer

def main():
    v, c, r = load_state("data")
    while True:
        print("\n1. Staff\n2. Customer Login\n3. Register\n4. Exit")
        entered_choice = input("Choice: ")
        if entered_choice == '1':
            print("1. Add Vehicle\n2. Backup")
            x = input("Select: ")
            if x == '1':
                add_vehicle(v, {"id": input("ID: "), "make": input("Make: "), "status": "available"})
                save_state("data", v, c, r)
            elif x == '2': backup_state("data", "backups")
        elif entered_choice == '2':
            user = authenticate_customer(c, input("Lic: "), input("Pin: "))
            if user: print("Hello " + user['name'])
        elif entered_choice == '3':
            register_customer(c, {"id": str(len(c)+1), "name": input("Name: "), "license_number": input("Lic: "), "pin": input("Pin: ")})
            save_state("data", v, c, r)
        elif entered_choice == '4':
            break

if __name__ == "__main__":
    main()