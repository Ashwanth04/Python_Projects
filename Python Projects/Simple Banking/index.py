class ATM: 
    def __init__(self): 
        self.Balance=10000 
        self.Acc= None 
    def deposit(self,amt): 
        self.Balance +=amt 
        print(amt,"is deposited successfully.") 
        print("Your Current Balance is ",self.Balance) 
    def withdrawal(self,amt): 
        if amt> self.Balance: 
            print("Insufficient funds!") 
        else: 
            self.Balance -= amt 
            print(amt," is Withdrawal Successfully.") 
        print("Your Current Balance is ",self.Balance) 
    def last(self): 
        print("Thank You!....") 
        print("Your Balance is:",self.Balance) 
        print("Account Number:xxx"+self.Acc+"xxx") 
        print("See You Again!..") 
        print("Have A Nice Day") 
atm = ATM() 
Acc = input("Enter Your Account Number:") 
pin=int(input("Enter Your Pin Number:")) 
name=input("Enter Your Name:") 
 
 
 
if Acc == "M314682I": 
    atm.Acc=Acc 
    if pin== 9854: 
        atm.pin=pin 
        print("Successfully Logged In") 
        while True: 
            print("Welcome To Magadha Bank") 
            print("1.Balance") 
            print("2.Credited Amount") 
            print("3.Amount Withdrawal") 
            print("4.Change Pin Number") 
            print("5.Exist") 
            choice=int(input("Press The Button According To Your 
Need ")) 
            if choice==1: 
                print("Your Current Balance is ",atm.Balance) 
            elif choice == 2: 
                amt=int(input("Enter the Amount to be Credit.")) 
                atm.deposit(amt) 
                atm.last() 
            elif choice == 3: 
                amt=int(input("Enter the Amount ")) 
                atm.withdrawal(amt) 
                atm.last() 
            elif choice == 4: 
                a=input("Enter Your Mobile Number:") 
            elif choice == 5: 
                atm.last() 
                break 
 
    else: 
        print("Invalid Pin") 
else: 
    print("Invalid Account Number") 