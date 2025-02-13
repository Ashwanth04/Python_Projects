currency = { 
    "INR": 1, "EUR": 0.0109, "USD": 0.0119, "SGD": 0.0158, 
    "AUD": 0.01812, "JPY": 1.7463, "CAD": 0.01635, "RUB": 
1.0536, 
    "PKR": 3.3192, "NZD": 0.01986, "GBP": 0.009335 
} 
 
def currency_converter(fromm, to, amount): 
    if fromm in currency and to in currency: 
        india = amount / currency[fromm] 
        convert_amount = india * currency[to] 
        return f"{amount} {fromm} is converted to 
{convert_amount:.2f} {to}" 
    else: 
        return "INVALID CURRENCY CODE" 
 
def menu(): 
    print("\nCURRENCY CONVERTER") 
    print("1. Convert Currency") 
    print("2. Exit") 
 
def main(): 
    while True: 
        menu() 
        try: 
            choice = int(input("Enter your choice: ")) 
            if choice == 1: 
                amount = float(input("Enter the amount: ")) 
                print("Available currencies: ", ", ".join(currency.keys())) 
                fromm = input("Enter your currency: ").upper() 
                to = input("Enter currency to convert to: ").upper() 
                print(currency_converter(fromm, to, amount)) 
 
            elif choice == 2: 
                print("Thanks For Visiting!....") 
                break 
            else: 
                print("Invalid choice. Please enter 1 or 2.") 
        except ValueError: 
            print("Invalid input. Please enter a number.") 
 
if __name__ == "__main__": 
    main() 