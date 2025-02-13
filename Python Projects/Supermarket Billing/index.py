def display_cart(cart): 
    print("\n--- SUPERMARKET BILLING SYSTEM ---") 
    print("NO | ITEM NAME | PRICE | QUANTITY | ITEM TOTAL") 
    print("-" * 50) 
    total_amount = 0 
    for i, (name, price, quantity) in enumerate(cart): 
        item_total = price * quantity 
        print(f"{i} | {name} | {price} | {quantity} | {item_total}") 
        total_amount += item_total 
    print("-" * 50) 
    return total_amount 
 
def remove_item(cart): 
    while True: 
        try: 
            item_no = int(input("\nEnter item number to remove 
(Enter 111 to stop): ")) 
            if item_no == 111: 
                break 
            elif 0 <= item_no < len(cart): 
                cart.pop(item_no) 
                print("Item removed successfully!") 
 
 
  
 
 
            else: 
                print("Invalid item number. Try again.") 
        except ValueError: 
            print("Please enter a valid number.") 
 
def checkout(cart): 
    total_amount = display_cart(cart) 
    discount = total_amount * 0.05  # 5% discount 
    discounted_amount = total_amount - discount 
    gst = discounted_amount * 0.18  # 18% GST 
    final_amount = discounted_amount + gst 
    print(f"\nTOTAL AMOUNT: {total_amount}") 
    print(f"DISCOUNT AMOUNT (5%): {discount}") 
    print(f"AMOUNT AFTER DISCOUNT: {discounted_amount}") 
    print(f"GST (18%): {gst}") 
    print(f"FINAL AMOUNT TO PAY: {final_amount}") 
    print("\nThank you for shopping with us!") 
 
def main(): 
    cart = [] 
    print("\nWelcome to Supermarket Billing System") 
    while True: 
        item_name = input("\nITEM NAME (type 'over' to stop 
adding): ") 
        if item_name.lower() == 'over': 
            break 
 
 
  
try: 
            item_price = int(input("ITEM PRICE: ")) 
            item_quantity = int(input("ITEM QUANTITY: ")) 
            cart.append((item_name, item_price, item_quantity)) 
        except ValueError: 
            print("Invalid input! Please enter valid numbers for price and 
quantity.") 
 
    while True: 
        total_amount = display_cart(cart) 
 
        print("\nOptions: \n1 - Proceed to Payment \n2 - Remove an 
Item \n3 - Add More Items \n4 - Exit") 
        try: 
            choice = int(input("\nEnter your choice: ")) 
            if choice == 1: 
                checkout(cart) 
                break 
            elif choice == 2: 
                remove_item(cart) 
            elif choice == 3: 
                return main()  # Restart the process to add items 
            elif choice == 4: 
                print("Thank you for visiting! Goodbye!") 
                break 
             
              else: 
                 print("Invalid choice! Try again.") 
             except ValueError: 
                 print("Please enter a valid number.") 
 
            main()