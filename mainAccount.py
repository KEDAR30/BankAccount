import datetime

class Account:
    pin =0000
    balance = 00000
    pin_data=[1111,2222,3333,4444]

    def __init__(self,_pin=1111):
        self._pin=_pin

    def Validate_pin(self):
        for x in self.pin_data:
            if x == self._pin:
                return True
            else:
                return False


    def deposit(self,amount):
        self.amount=amount
        self.balance +=  amount 
        print("amount deposited:",amount)
        x=Transaction_History("Money deposited: ", amount)
        x.Record_tr_details()

    def withdraw(self,amount):
        self.amount= amount
        if self.balance>= amount:
            self.balance-= amount
            print("amount withdrawn:",amount)
            x=Transaction_History("Money withdrawn: ", amount)
            x.Record_tr_details()
        else:
            print("insufficient balance")

    def check_balance(self):
        print("Current balance:",self.balance)

class CheckingAccount(Account):
    def __init__(self):
        super(CheckingAccount,self).__init__()
        
    def deposit(self, amount):
        return super().deposit(amount)

    def withdraw(self, amount):
        return super().withdraw(amount)

    def check_balance(self):
        return super().check_balance()

class SavingAccount(Account):
    def __init__(self):
        super(SavingAccount,self).__init__()

    def deposit(self, amount):
        return super().deposit(amount)

    def withdraw(self, amount):
        return super().withdraw(amount)

    def check_balance(self):
        return super().check_balance()
        

class BusinessAccount(Account):
    def __init__(self):
        super(BusinessAccount,self).__init__()

    def deposit(self, amount):
        return super().deposit(amount)

    def withdraw(self, amount):
        return super().withdraw(amount)
    
    def check_balance(self):
        return super().check_balance()

    
class Transaction_History:
    current_time_date =""
    transaction_mode=""
    def __init__(self,tr_mode):
        self.current_time_date=datetime.datetime.now()
        self.transction_mode=tr_mode

    def Record_tr_details(self):
        file=open("Tr_history.txt","r+")
        file.write("Date Time:" , self.current_time_date , " " + "Transction Mode:" , self.transction_mode )

    def Show_transaction_history(self):
        file=open("Tr_history.txt","r")
        data=file.read()
        print(data)

class Atm_Logic:
    def __init__(self,message):
        print(message)
        print("-------------Welcome------------")

    def CheckingAccount_Functions(self):
        print("------------Application------------")
        print("1)Check Balance")
        print("2)Deposit Money")
        print("3)Withdrw Money")
        print("4)Transanction History")
        print("5)Exit")
        option = str(input("Please select one of the above:"))
        if option != "":
            Chk = CheckingAccount()
            if option == "1":
                Chk.check_balance()
            elif option == "2":
                amount = int(input("Enter the amount:"))
                Chk.deposit(amount)
            elif option == "3":
                amount = int(input("Enter the amount:"))
                Chk.withdraw(amount)
            elif option == "4":
                tr = Transaction_History("")
                tr.Show_transaction_history()
            elif option == "5":
                print("Thank You!!")

    def SavingAccount_Functions(self):
        print("------------Application------------")
        print("1)Check Balance")
        print("2)Deposit Money")
        print("3)Withdrw Money")
        print("4)Transanction History")
        print("5)Exit")

        option = str(input("Please select one of the above:"))
        if option != "":
            Svg = SavingAccount()
            if option == "1":
                Svg.check_balance()
            elif option == "2":
                amount = int(input("Enter the amount:"))
                Svg.deposit(amount)
            elif option == "3":
                amount = int(input("Enter the amount:"))
            Svg.withdraw(amount)
        elif option == "4":
            tr = Transaction_History("")
            tr.Show_transaction_history()
        elif option == "5":
            print("Thank You!!")

    def BusniessAccount_Functions(self):
        print("------------Application------------")
        print("1)Check Balance")
        print("2)Deposit Money")
        print("3)Withdrw Money")
        print("4)Transanction History")
        print("5)Exit")

        option = str(input("Please select one of the above:"))
        if option != "":
            Bsg = BusinessAccount()
            if option == "1":
                Bsg.check_balance()
            elif option == "2":
                amount = int(input("Enter the amount:"))
                Bsg.deposit(amount)
            elif option == "3":
                amount = int(input("Enter the amount:"))
                Bsg.withdraw(amount)
            elif option == "4":
                tr = Transaction_History("")
                tr.Show_transaction_history()
            elif option == "5":
                print("Thank You!!")


    

        


    



    






    
        

        

