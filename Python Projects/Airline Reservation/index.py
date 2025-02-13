import mysql.connector 
from datetime import datetime 
 
def establish_database_connection(): 
    try: 
        connection = mysql.connector.connect( 
            host="localhost", 
            user="root",  # replace with your MySQL username 
            password="",  # replace with your MySQL password 
            database="airline resevation"  # your database name 
        ) 
        return connection 
    except mysql.connector.Error as err: 
        print(f"Error: {err}") 
        return None 
 
class RESERVATION: 
    def __init__(self): 
        print("WELCOME TO Flying Squad Airlines") 
        self.name = '' 
        self.age = '' 
        self.address = '' 
        self.passport = '' 
        self.mobile = '' 
        self.bord = '' 
        self.des = '' 
        self.amount = 0 
        self.travel_date = None  # Add a travel_date field 
 
    def select_destination_and_tickets(self): 
        # Predefined available boarding points and destinations 
        boarding_points = ["New York", "Los Angeles", "Sydney", "Ontorio"] 
 
        destinations = ["Chennai", "Trichy", "Bangalore", 
"Trivandrum"] 
 
        print("Available Boarding Points:") 
        for point in boarding_points: 
            print(f"{point}") 
 
        print("\nAvailable Destinations:") 
        for dest in destinations: 
            print(f"{dest}") 
 
        while True: 
            self.bord = input("Select Your Boarding Point (Choose 
from the list above): ") 
            if self.bord not in boarding_points: 
                print("Invalid Boarding Point. Please select a valid 
one.") 
                continue 
            break 
 
        while True: 
            self.des = input("Select Your Destination (Choose from 
the list above): ") 
 
 
 
 
            if self.des not in destinations: 
                print("Invalid Destination. Please select a valid one.") 
                continue 
            break 
 
        num_tickets = int(input("Enter the number of tickets: ")) 
        self.calculate_ticket_amount(num_tickets) 
 
        confirm = input("Do you want to confirm the ticket(s)? 
(yes/no): ").strip().lower() 
 
        if confirm == "yes": 
            self.confirm_ticket(num_tickets) 
        else: 
            print("Ticket(s) not confirmed.") 
 
    def calculate_ticket_amount(self, num_tickets): 
 
        special_routes = { 
            ("New York", "Chennai"): 14000, 
            ("New York", "Trichy"): 13000, 
            ("New York", "Bangalore"): 21000, 
            ("New York", "Trivandrum"): 13000, 
 
 
            ("Los Angeles", "Chennai"): 10000, 
            ("Los Angeles", "Trichy"): 18000, 
            ("Los Angeles", "Bangalore"): 19500, 
            ("Los Angeles", "Trivandrum"): 15000, 
            ("Sydney", "Chennai"): 20000, 
            ("Sydney", "Trichy"): 10000, 
            ("Sydney", "Bangalore"): 22000, 
            ("Sydney", "Trivandrum"): 19000, 
            ("Ontorio", "Chennai"): 30000, 
            ("Ontorio", "Trichy"): 29000, 
            ("Ontorio", "Bangalore"): 31000, 
            ("Ontorio", "Trivandrum"): 20000 
        } 
 
        if (self.bord, self.des) in special_routes: 
            self.amount = special_routes[(self.bord, self.des)] * num_tickets 
            print(f"Base ticket amount for {num_tickets} ticket(s): 
{self.amount}") 
        else: 
            print("Invalid boarding or destination station.") 
            self.amount = 0 
 
 
    def confirm_ticket(self, num_tickets): 
        connection = establish_database_connection() 
        if connection is None: 
            return 
 
 
 
 
 
        extra_luggage = input("Do you have extra luggage? 
(yes/no): ").strip().lower() 
        if extra_luggage == "yes": 
            extra_charge = int(input("Enter extra luggage charges: ")) 
            self.amount += extra_charge 
 
       
        self.name = input("Enter Your Name: ") 
        self.age = input("Enter Your Age: ") 
        self.address = input("Enter Your Address: ") 
        self.passport = input("Enter Your Passport Number: ") 
        self.mobile = input("Enter Your Phone Number: ") 
 
        
        cursor = connection.cursor() 
        sql = """INSERT INTO airline (name, age, address, passport, 
mobile, bord, des, amount)  
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s)""" 
        data = (self.name, self.age, self.address, self.passport, 
self.mobile, self.bord, self.des, self.amount) 
 
        cursor.execute(sql, data) 
        connection.commit() 
 
 
        print( 
            f"Ticket(s) confirmed. Passport: {self.passport}, Boarding: 
{self.bord}, Destination: {self.des}, Amount: {self.amount}") 
        print("Thank You!.. Have a great Journey!...") 
 
        cursor.close() 
        connection.close() 
 
    def cancel_ticket(self): 
        connection = establish_database_connection() 
        if connection is None: 
            return 
 
        passport = input("Enter your Passport Number to cancel the 
ticket: ") 
 
        cursor = connection.cursor() 
        sql = "DELETE FROM airline WHERE passport = %s" 
        cursor.execute(sql, (passport,)) 
        connection.commit() 
 
        if cursor.rowcount > 0: 
            print(f"Ticket with Passport Number {passport} has been 
canceled successfully.") 
        else: 
            print("No ticket found with the provided Passport Number.") 
 
 
 
        cursor.close() 
        connection.close() 
 
    def change_travel_date(self): 
        connection = establish_database_connection() 
        if connection is None: 
            return 
 
        passport = input("Enter your Passport Number to change the 
travel date: ") 
 
        new_travel_date = input("Enter the new travel date (YYYY
MM-DD): ") 
 
        try:  
            datetime.strptime(new_travel_date, "%Y-%m-%d") 
        except ValueError: 
            print("Invalid date format. Please use YYYY-MM-DD.") 
            return 
 
        cursor = connection.cursor() 
        sql = "UPDATE airline SET travel_date = %s WHERE passport 
= %s" 
        cursor.execute(sql, (new_travel_date, passport)) 
        connection.commit() 
 
 
 
        if cursor.rowcount > 0: 
            print(f"Travel date for Passport Number {passport} has been 
updated to {new_travel_date}.") 
        else: 
            print("No ticket found with the provided Passport Number.") 
 
        cursor.close() 
        connection.close() 
 
if __name__ == "__main__": 
    reservation = RESERVATION() 
    while True: 
        print("\nMenu:") 
        print("1. Select Destination and Number of Tickets") 
        print("2. Cancel Ticket") 
        print("3. Change Travel Date") 
        print("4. Exit") 
 
        choice = input("Enter your choice: ").strip() 
 
        if choice == "1": 
            reservation.select_destination_and_tickets() 
        elif choice == "2": 
            reservation.cancel_ticket() 
        elif choice == "3": 
            reservation.change_travel_date() 
 
 
 
 
 
        elif choice == "4": 
            print("Thank you! Visit Again!") 
            break 
        else: 
            print("Invalid choice. Please try again.")