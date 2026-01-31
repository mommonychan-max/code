import json
import os
from datetime import datetime

DATA_FILE = "transport_data.json"

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return {
        "customers": [],
        "drivers": [],
        "vehicles": [],
        "shipments": []
    }

def save_data(data):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def input_non_empty(prompt):
    while True:
        s = input(prompt).strip()
        if s:
            return s
        print("❌ សូមបញ្ចូលអោយបានត្រឹមត្រូវ (មិនអាចទទេ)")

def input_int(prompt):
    while True:
        try:
            return int(input(prompt).strip())
        except:
            print("❌ សូមបញ្ចូលជាលេខ (integer)")

def input_float(prompt):
    while True:
        try:
            return float(input(prompt).strip())
        except:
            print("❌ សូមបញ្ចូលជាលេខ (float)")

def find_by_id(items, key, value):
    for item in items:
        if item.get(key) == value:
            return item
    return None

def print_table(items, title):
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)
    if not items:
        print("⚠️ មិនមានទិន្នន័យ")
        return
    for i, item in enumerate(items, 1):
        print(f"{i}. {item}")
    print("=" * 60)

# ------------------ Customers ------------------
def add_customer(data):
    cid = input_non_empty("Customer ID: ")
    if find_by_id(data["customers"], "id", cid):
        print("❌ ID នេះមានរួចហើយ")
        return
    name = input_non_empty("Name: ")
    phone = input_non_empty("Phone: ")
    address = input_non_empty("Address: ")
    data["customers"].append({"id": cid, "name": name, "phone": phone, "address": address})
    save_data(data)
    print("✅ បន្ថែមអតិថិជនរួចរាល់")

def edit_customer(data):
    cid = input_non_empty("Enter Customer ID to edit: ")
    c = find_by_id(data["customers"], "id", cid)
    if not c:
        print("❌ រកមិនឃើញ Customer")
        return
    print("ចុច Enter ដើម្បីរក្សាទុកតម្លៃចាស់")
    name = input("New Name: ").strip()
    phone = input("New Phone: ").strip()
    address = input("New Address: ").strip()
    if name: c["name"] = name
    if phone: c["phone"] = phone
    if address: c["address"] = address
    save_data(data)
    print("✅ កែប្រែរួចរាល់")

def delete_customer(data):
    cid = input_non_empty("Enter Customer ID to delete: ")
    c = find_by_id(data["customers"], "id", cid)
    if not c:
        print("❌ រកមិនឃើញ Customer")
        return
    data["customers"].remove(c)
    save_data(data)
    print("✅ លុបរួចរាល់")

# ------------------ Drivers ------------------
def add_driver(data):
    did = input_non_empty("Driver ID: ")
    if find_by_id(data["drivers"], "id", did):
        print("❌ ID នេះមានរួចហើយ")
        return
    name = input_non_empty("Name: ")
    phone = input_non_empty("Phone: ")
    license_no = input_non_empty("License No: ")
    data["drivers"].append({"id": did, "name": name, "phone": phone, "license": license_no})
    save_data(data)
    print("✅ បន្ថែមអ្នកបើកបរ រួចរាល់")

def edit_driver(data):
    did = input_non_empty("Enter Driver ID to edit: ")
    d = find_by_id(data["drivers"], "id", did)
    if not d:
        print("❌ រកមិនឃើញ Driver")
        return
    print("ចុច Enter ដើម្បីរក្សាទុកតម្លៃចាស់")
    name = input("New Name: ").strip()
    phone = input("New Phone: ").strip()
    license_no = input("New License No: ").strip()
    if name: d["name"] = name
    if phone: d["phone"] = phone
    if license_no: d["license"] = license_no
    save_data(data)
    print("✅ កែប្រែរួចរាល់")

def delete_driver(data):
    did = input_non_empty("Enter Driver ID to delete: ")
    d = find_by_id(data["drivers"], "id", did)
    if not d:
        print("❌ រកមិនឃើញ Driver")
        return
    data["drivers"].remove(d)
    save_data(data)
    print("✅ លុបរួចរាល់")

# ------------------ Vehicles ------------------
def add_vehicle(data):
    vid = input_non_empty("Vehicle ID: ")
    if find_by_id(data["vehicles"], "id", vid):
        print("❌ ID នេះមានរួចហើយ")
        return
    plate = input_non_empty("Plate Number: ")
    vtype = input_non_empty("Vehicle Type (truck/van/...): ")
    capacity = input_float("Capacity (kg): ")
    data["vehicles"].append({"id": vid, "plate": plate, "type": vtype, "capacity_kg": capacity})
    save_data(data)
    print("✅ បន្ថែមយានយន្តរួចរាល់")

def edit_vehicle(data):
    vid = input_non_empty("Enter Vehicle ID to edit: ")
    v = find_by_id(data["vehicles"], "id", vid)
    if not v:
        print("❌ រកមិនឃើញ Vehicle")
        return
    print("ចុច Enter ដើម្បីរក្សាទុកតម្លៃចាស់")
    plate = input("New Plate: ").strip()
    vtype = input("New Type: ").strip()
    cap = input("New Capacity (kg): ").strip()
    if plate: v["plate"] = plate
    if vtype: v["type"] = vtype
    if cap:
        try:
            v["capacity_kg"] = float(cap)
        except:
            print("⚠️ Capacity មិនត្រឹមត្រូវ ដូច្នេះរក្សាទុកតម្លៃចាស់")
    save_data(data)
    print("✅ កែប្រែរួចរាល់")

def delete_vehicle(data):
    vid = input_non_empty("Enter Vehicle ID to delete: ")
    v = find_by_id(data["vehicles"], "id", vid)
    if not v:
        print("❌ រកមិនឃើញ Vehicle")
        return
    data["vehicles"].remove(v)
    save_data(data)
    print("✅ លុបរួចរាល់")

# ------------------ Shipments / Orders ------------------
def add_shipment(data):
    sid = input_non_empty("Shipment ID: ")
    if find_by_id(data["shipments"], "id", sid):
        print("❌ ID នេះមានរួចហើយ")
        return

    cust_id = input_non_empty("Customer ID: ")
    if not find_by_id(data["customers"], "id", cust_id):
        print("❌ Customer ID មិនមានក្នុងប្រព័ន្ធ")
        return

    driver_id = input_non_empty("Driver ID: ")
    if not find_by_id(data["drivers"], "id", driver_id):
        print("❌ Driver ID មិនមានក្នុងប្រព័ន្ធ")
        return

    vehicle_id = input_non_empty("Vehicle ID: ")
    if not find_by_id(data["vehicles"], "id", vehicle_id):
        print("❌ Vehicle ID មិនមានក្នុងប្រព័ន្ធ")
        return

    origin = input_non_empty("From (Origin): ")
    destination = input_non_empty("To (Destination): ")
    weight = input_float("Weight (kg): ")
    price = input_float("Price ($): ")

    status = "Pending"  # Pending, In Transit, Delivered, Cancelled
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data["shipments"].append({
        "id": sid,
        "customer_id": cust_id,
        "driver_id": driver_id,
        "vehicle_id": vehicle_id,
        "origin": origin,
        "destination": destination,
        "weight_kg": weight,
        "price_usd": price,
        "status": status,
        "created_at": created_at
    })
    save_data(data)
    print("✅ បង្កើតការដឹកជញ្ជូនរួចរាល់")

def update_shipment_status(data):
    sid = input_non_empty("Enter Shipment ID: ")
    s = find_by_id(data["shipments"], "id", sid)
    if not s:
        print("❌ រកមិនឃើញ Shipment")
        return
    print("1) Pending\n2) In Transit\n3) Delivered\n4) Cancelled")
    choice = input_non_empty("Choose new status: ")
    mapping = {"1": "Pending", "2": "In Transit", "3": "Delivered", "4": "Cancelled"}
    if choice not in mapping:
        print("❌ ជម្រើសមិនត្រឹមត្រូវ")
        return
    s["status"] = mapping[choice]
    save_data(data)
    print("✅ Update status រួចរាល់")

def search_shipments(data):
    key = input_non_empty("Search by (id/customer/driver/vehicle/status): ").lower()
    value = input_non_empty("Value: ")

    results = []
    for s in data["shipments"]:
        if key == "id" and s["id"] == value:
            results.append(s)
        elif key == "customer" and s["customer_id"] == value:
            results.append(s)
        elif key == "driver" and s["driver_id"] == value:
            results.append(s)
        elif key == "vehicle" and s["vehicle_id"] == value:
            results.append(s)
        elif key == "status" and s["status"].lower() == value.lower():
            results.append(s)

    print_table(results, "Search Results (Shipments)")

# ------------------ Reports ------------------
def report_summary(data):
    total_shipments = len(data["shipments"])
    total_income = sum(s["price_usd"] for s in data["shipments"] if s["status"] != "Cancelled")
    delivered = sum(1 for s in data["shipments"] if s["status"] == "Delivered")
    in_transit = sum(1 for s in data["shipments"] if s["status"] == "In Transit")
    pending = sum(1 for s in data["shipments"] if s["status"] == "Pending")
    cancelled = sum(1 for s in data["shipments"] if s["status"] == "Cancelled")

    print("\n" + "=" * 60)
    print("REPORT SUMMARY")
    print("=" * 60)
    print(f"Total shipments : {total_shipments}")
    print(f"Delivered       : {delivered}")
    print(f"In Transit      : {in_transit}")
    print(f"Pending         : {pending}")
    print(f"Cancelled       : {cancelled}")
    print(f"Total income($) : {total_income:.2f}")
    print("=" * 60)

# ------------------ Menus ------------------
def menu_customers(data):
    while True:
        print("\n--- Customers Menu ---")
        print("1) Add Customer")
        print("2) View Customers")
        print("3) Edit Customer")
        print("4) Delete Customer")
        print("0) Back")
        ch = input("Choose: ").strip()
        if ch == "1": add_customer(data)
        elif ch == "2": print_table(data["customers"], "Customers")
        elif ch == "3": edit_customer(data)
        elif ch == "4": delete_customer(data)
        elif ch == "0": break
        else: print("❌ ជម្រើសមិនត្រឹមត្រូវ")

def menu_drivers(data):
    while True:
        print("\n--- Drivers Menu ---")
        print("1) Add Driver")
        print("2) View Drivers")
        print("3) Edit Driver")
        print("4) Delete Driver")
        print("0) Back")
        ch = input("Choose: ").strip()
        if ch == "1": add_driver(data)
        elif ch == "2": print_table(data["drivers"], "Drivers")
        elif ch == "3": edit_driver(data)
        elif ch == "4": delete_driver(data)
        elif ch == "0": break
        else: print("❌ ជម្រើសមិនត្រឹមត្រូវ")

def menu_vehicles(data):
    while True:
        print("\n--- Vehicles Menu ---")
        print("1) Add Vehicle")
        print("2) View Vehicles")
        print("3) Edit Vehicle")
        print("4) Delete Vehicle")
        print("0) Back")
        ch = input("Choose: ").strip()
        if ch == "1": add_vehicle(data)
        elif ch == "2": print_table(data["vehicles"], "Vehicles")
        elif ch == "3": edit_vehicle(data)
        elif ch == "4": delete_vehicle(data)
        elif ch == "0": break
        else: print("❌ ជម្រើសមិនត្រឹមត្រូវ")

def menu_shipments(data):
    while True:
        print("\n--- Shipments Menu ---")
        print("1) Create Shipment")
        print("2) View Shipments")
        print("3) Update Shipment Status")
        print("4) Search Shipments")
        print("0) Back")
        ch = input("Choose: ").strip()
        if ch == "1": add_shipment(data)
        elif ch == "2": print_table(data["shipments"], "Shipments / Orders")
        elif ch == "3": update_shipment_status(data)
        elif ch == "4": search_shipments(data)
        elif ch == "0": break
        else: print("❌ ជម្រើសមិនត្រឹមត្រូវ")

def main():
    data = load_data()
    while True:
        print("\n" + "=" * 60)
        print("TRANSPORT COMPANY INFORMATION SYSTEM (Python)")
        print("=" * 60)
        print("1) Customers")
        print("2) Drivers")
        print("3) Vehicles")
        print("4) Shipments / Orders")
        print("5) Report Summary")
        print("0) Exit")
        ch = input("Choose: ").strip()

        if ch == "1": menu_customers(data)
        elif ch == "2": menu_drivers(data)
        elif ch == "3": menu_vehicles(data)
        elif ch == "4": menu_shipments(data)
        elif ch == "5": report_summary(data)
        elif ch == "0":
            print("👋 Bye!")
            break
        else:
            print("❌ ជម្រើសមិនត្រឹមត្រូវ")

if __name__ == "__main__":
    main()

