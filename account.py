class Account:
    def __init__(self, number,pin):
        self.number = number
        self.__pin =pin
        self.__balance= 0
        self._transactions=[]
        self.owner= owner
        self.limit = limit
        self.interest= interest
    def show__balance(self, pin):
        if pin == self.__pin:
           return  self.__balance

        else :
            return "wrong pin"
    
    def deposit(self,amount,pin):
        if pin==self.__pin:
            self.__balance+=amount
            self._transactions.append(f"Deposit:{amount}")
            return f"Ksh {amount} was deposited successfully. Current balance is Ksh {self.__balance} "
        
        else:
            return f"Please enter the correct pin"


    def withdrawal(self,amount, pin):
        if pin ==self.__pin:
            if self.__balance <=100:
                return f"The balance is too small to be withdrawn"
            
            else:
                self.__balance-=amount
            return f"you have successfully withdrawn {amount} and your new balance is {self.__balance}"

        else:
                return f"input correct password"


    def owner_account_details(self,pin):
        if pin!= self._pin:
            return f"Wrong pin"
        else:
            return{
           
                "Owner": self.owner,
                "Balance": self.__balance,
                "transaction": self._transactions

            }
        
    def change_account_owner(self, new_owner, pin):
        if pin!= self.__pin:
            return "Wrong pin"
        self.owner = new_owner
        return f"The new account owner is {new_owner}"

    def account_statement(self,new_owner, amount):
        return f"You have successfully transfer ksh {amout} and your new balance is {self.__balance}"
    
    def overdraft_limit(self,limit):
         self.overdraft_limit = limit
         return f"Your overdraft limit is {limit}"
    

    def interest_calculation():
            interest = self.__balance * rate / 100
            self.__balance += interest
            self.transactions.append(f"Interest added: {interest}")
            return f"Interest calculated and applied. New balance: {self.__balance}"






