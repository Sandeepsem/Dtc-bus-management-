import mysql.connector 
import pandas as pd 
import matplotlib.pyplot as plt 
from tabulate import tabulate 
 
# ================= DATABASE CONNECTION ================= 
def connect_db(): 
    return mysql.connector.connect( 
        host="localhost", 
        user="root", 
        password="", 
        database="dtc_bus_service1" 
    ) 
 
# ================= HELPER FUNCTION ================= 
def show_dataframe(rows, columns, title): 
    if not rows: 
        print(f"\nNo records found for {title}.\n") 
        return 
    print(f"\n========== {title.upper()} ==========\n") 
    df = pd.DataFrame(rows, columns=columns) 
    print(tabulate(df, headers="keys", tablefmt="grid", numalign="center", stralign="center", 
showindex=False)) 
    print("\n") 
 
# ================= USER PANEL FUNCTIONS ================= 
def user_view_all_buses(): 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("SELECT * FROM bus") 
    rows = cur.fetchall() 
    db.close() 
    show_dataframe(rows, ["Bus No", "Source", "Destination", "Route", "Stops", "Time (mins)", 
"Fare (₹)"], "All Buses") 
 
def user_search_bus_by_number(): 
    bus_no = input("Enter Bus Number: ").upper() 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("SELECT * FROM bus WHERE bus_no=%s", (bus_no,)) 
    rows = cur.fetchall() 
    db.close() 
    show_dataframe(rows, ["Bus No", "Source", "Destination", "Route", "Stops", "Time (mins)", 
"Fare (₹)"], f"Bus {bus_no}") 
 
def user_search_between_stops(): 
    start = input("Enter starting stop: ").strip().lower() 
    end = input("Enter destination stop: ").strip().lower() 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("SELECT * FROM bus") 
    rows = [r for r in cur.fetchall() if start in r[4].lower() and end in r[4].lower()] 
    db.close() 
    show_dataframe(rows, ["Bus No", "Source", "Destination", "Route", "Stops", "Time", "Fare"], 
f"Buses between {start} and {end}") 
 
def user_search_passing_stop(): 
    stop = input("Enter stop name: ").strip().lower() 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("SELECT * FROM bus") 
    rows = [r for r in cur.fetchall() if stop in r[4].lower()] 
    db.close() 
    show_dataframe(rows, ["Bus No", "Source", "Destination", "Route", "Stops", "Time", "Fare"], 
f"Buses passing through {stop}") 
 
def user_add_feedback(): 
    bus_no = input("Enter Bus Number: ").upper() 
    rating = int(input("Enter Rating (1–5): ")) 
    feedback = input("Enter Feedback: ") 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("INSERT INTO customer_feedback (bus_no, rating, feedback) VALUES (%s, %s, %s), (bus_no, rating, feedback)") 
    db.commit() 
    db.close() 
    print("✅Thank you! Feedback submitted successfully.\n") 
 
# ================= ADMIN PANEL FUNCTIONS ================= 
def admin_login(): 
    username = input("Enter Admin Username: ") 
    password = input("Enter Admin Password: ") 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("SELECT * FROM admin WHERE username=%s AND password=%s", 
(username, password)) 
    if cur.fetchone(): 
        print("\n✅ Login successful!\n") 
        admin_menu() 
    else: 
        print("\n ❌ Invalid credentials.\n") 
    db.close() 
 
def admin_view_all_buses(): 
    user_view_all_buses() 
 
def admin_add_bus(): 
    data = input("Enter bus_no, source, destination, route, stops, time, fare (comma-separated):").split(',') 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("INSERT INTO bus VALUES (%s,%s,%s,%s,%s,%s,%s)", tuple(map(str.strip,data))) 
    db.commit() 
    db.close() 
    print(" ✅ Bus added successfully.\n") 
 
def admin_delete_bus(): 
    bus_no = input("Enter Bus Number to delete: ").upper() 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("DELETE FROM bus WHERE bus_no=%s", (bus_no,)) 
    db.commit() 
    db.close() 
    print(" 🗑 Bus deleted successfully.\n") 
 
def admin_view_staff(): 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("SELECT bus_no, driver, conductor, marshal, rounds_per_day, timing FROM staff") 
    rows = cur.fetchall() 
    db.close() 
    show_dataframe(rows, ["Bus No", "Driver", "Conductor", "Marshal", "Rounds/Day", "Timing"], "Bus Staff Details") 
 
def admin_add_staff(): 
    data = input("Enter bus_no, driver, conductor, marshal, rounds_per_day, timing (comma-separated): ").split(',') 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("INSERT INTO staff (bus_no, driver, conductor, marshal, rounds_per_day, timing)VALUES (%s,%s,%s,%s,%s,%s)", tuple(map(str.strip, data))) 
    db.commit() 
    db.close() 
    print(" ✅ Staff added successfully.\n") 
 
def admin_view_earnings(): 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("SELECT bus_no, fare, stops FROM bus") 
    bus_data = cur.fetchall() 
    cur.execute("SELECT bus_no, rounds_per_day FROM staff") 
    staff_data = dict(cur.fetchall()) 
    db.close() 
 
    avg_passengers = 30 
    earnings = [] 
    for bus_no, fare, stops in bus_data: 
        rounds = staff_data.get(bus_no, 1) 
        total = fare * (len(stops.split(','))) * avg_passengers * rounds 
        earnings.append((bus_no, fare, rounds, avg_passengers, total)) 
    show_dataframe(earnings, ["Bus No", "Fare (₹)", "Rounds/Day", "Avg Passengers", "Daily Earning (₹)"], "Automatic Earnings Summary") 
 
def admin_view_feedback(): 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("SELECT bus_no, rating, feedback FROM customer_feedback") 
    rows = cur.fetchall() 
    db.close() 
    show_dataframe(rows, ["Bus No", "Rating (/5)", "Feedback"], "Customer Feedback") 
 
def admin_charts(): 
    db = connect_db() 
    cur = db.cursor() 
    cur.execute("SELECT bus_no, fare FROM bus") 
    df = pd.DataFrame(cur.fetchall(), columns=["Bus No", "Fare (₹)"]) 
    plt.bar(df["Bus No"], df["Fare (₹)"]) 
    plt.title("Bus Fare Comparison") 
    plt.xlabel("Bus No") 
    plt.ylabel("Fare (₹)") 
    plt.show() 
    db.close() 
 
# ================= MENU STRUCTURE ================= 
def user_menu(): 
    while True: 
        print("\n===== USER PANEL =====") 
        print("1. View All Buses") 
        print("2. Search Bus by Number") 
        print("3. Search Buses Between Two Stops") 
        print("4. Search Buses Passing Through Stop") 
        print("5. Add Feedback") 
        print("6. Back to Main Menu") 
        ch = input("Enter choice: ") 
        if ch == '1': user_view_all_buses() 
        elif ch == '2': user_search_bus_by_number() 
        elif ch == '3': user_search_between_stops() 
        elif ch == '4': user_search_passing_stop() 
        elif ch == '5': user_add_feedback() 
        elif ch == '6': break 
        else: print("Invalid choice!") 
 
def admin_menu(): 
    while True: 
        print("\n===== ADMIN PANEL =====") 
        print("1. View All Buses") 
        print("2. Add Bus") 
        print("3. Delete Bus") 
        print("4. View Staff") 
        print("5. Add Staff") 
        print("6. View Earnings Summary") 
        print("7. View Feedback") 
        print("8. Analytics Charts") 
        print("9. Logout") 
        ch = input("Enter choice: ") 
        if ch == '1': admin_view_all_buses() 
        elif ch == '2': admin_add_bus() 
        elif ch == '3': admin_delete_bus() 
        elif ch == '4': admin_view_staff() 
        elif ch == '5': admin_add_staff() 
        elif ch == '6': admin_view_earnings() 
        elif ch == '7': admin_view_feedback() 
        elif ch == '8': admin_charts() 
        elif ch == '9': break 
        else: print("Invalid choice!") 
 
def main(): 
    print("\n 🚍 Welcome to Delhi Transport Corporation (DTC) System�� ") 
    while True: 
        print("\n===== MAIN MENU =====") 
        print("1. User Panel") 
        print("2. Admin Login") 
        print("3. Exit") 
        ch = input("Enter choice: ") 
        if ch == '1': user_menu() 
        elif ch == '2': admin_login() 
        elif ch == '3': 
            print("Thank you for using DTC Bus Management System!") 
            break 
        else: print("Invalid choice!") 
 
# ================= RUN ================= 
if __name__ == "__main__": 
    main() 
