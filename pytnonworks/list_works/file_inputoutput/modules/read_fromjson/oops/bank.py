from datetime import datetime
class Bank:
    Bank_name=str
    acno:str
    person_name=str
    ac_type=str
    Balance=int
    def create(self,b_name,acno,p_name,ac_type,bal):
        self.Bank_name=b_name
        self.acno=acno
        self.person_name=p_name
        self.ac_type=ac_type
        self.Balance=bal
    def deposit(self,amount):
        self.Balance+=amount
        print(f"your{self.Bank_name}has beens credicted with{amount} avl bal is {self.Balance}")
    def withdrawal(self,amount):
        if amount>self.Balance:
          print("transaction failed")
        else:
           self.Balance-=amount
        print(f"your{self.Bank_name}has beens credicted with{amount} avl bal is {self.Balance}")
    def get_Balance(self):
        print(f"your{self.Bank_name} AC/{self.acno} bal on {datetime.today()} is {self.Balance}")

obj1=Bank()
obj1.create("sbi","10234","abhi","savings",4000)
obj1.deposit(2000)
obj1.withdrawal(1000)
obj1.get_Balance()
obj2=Bank()
obj2.create("sbi","10236","anu","savings",5000)


        