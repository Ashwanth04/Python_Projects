pharmacy = {} 
 
def add_medicine(name, price, quantity): 
    if name not in pharmacy: 
        pharmacy[name] = {"quantity": quantity, "price": price} 
        print(f"Added {quantity} units of {name} at ${price} each. 
Total amount: ${quantity * price}") 
    else: 
        current_quantity = pharmacy[name]["quantity"] 
        current_quantity += quantity 
        pharmacy[name].update({"quantity": current_quantity, 
"price": price}) 
        print(f"Added {quantity} units of {name}. Updated stock: 
{current_quantity} units. Price per unit: ${price}") 
 
 
def sell_medicine(name, quantity): 
    if name not in pharmacy: 
        print("This medicine is not available. Check later.") 
        return 
 
    if pharmacy[name]["quantity"] < quantity: 
        print(f"Only {pharmacy[name]['quantity']} units left in 
stock.") 
        return 
 
 
 
 
    pharmacy[name]["quantity"] -= quantity 
    total_amount = quantity * pharmacy[name]["price"] 
    print(f"Sold {quantity} units of {name}. Total amount: 
${total_amount}") 
 
 
def menu(): 
    print("\nPharmacy Management System") 
    print("1. Add Medicine") 
    print("2. Sell Medicine") 
    print("3. Show Inventory") 
    print("4. Exit") 
 
 
def show_inventory(): 
    print("\nCurrent Inventory:") 
    if not pharmacy: 
        print("No medicines available.") 
    else: 
        for name, details in pharmacy.items(): 
            print(f"{name}: {details['quantity']} units available at 
${details['price']} each.") 
 
 
def main(): 
    while True: 
        menu() 
        choice = int(input("Enter your choice: ")) 
 
 
 
        if choice == 1: 
            name = input("Enter Medicine Name: ") 
            price = float(input("Enter Price Per Unit: ")) 
            quantity = int(input("Enter Medicine Quantity: ")) 
            add_medicine(name, price, quantity) 
 
        elif choice == 2: 
            name = input("Enter Medicine Name: ") 
            quantity = int(input("Enter Quantity to Sell: ")) 
            sell_medicine(name, quantity) 
 
        elif choice == 3: 
            show_inventory() 
 
        elif choice == 4: 
            print("Exiting the system.") 
            break 
 
        else: 
            print("Invalid choice. Please select again.") 
 
main()