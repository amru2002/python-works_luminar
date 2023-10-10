from abc import ABC,abstractmethod
class Bankapp(ABC):
    @abstractmethod
    def fundtransfer(self):
        pass
    @abstractmethod
    def balanceenquiry(self):
        pass
    @abstractmethod
    def transactionhistory(self):
        pass
class Googlepay(Bankapp):
     def fundtransfer(self):
         print("google pay to fundtransfer")
     def balanceenquiry(self):
          print("google pay to balanceenquiry")
     def transactionhistory(self):
         print("google pay to transaction history")
obj=Googlepay()
obj.fundtransfer()

    