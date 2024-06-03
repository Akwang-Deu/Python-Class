class Account:
    def __init__(self, number,pin):
        self.number = number
        self.__pin =pin
        self.__balance= 0
        self._transactions=[]
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
