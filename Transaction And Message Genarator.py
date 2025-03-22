# Account credit and debit Transaction and Message Generator

class Account :
    def __init__(self,Bal,Acc):
        self.Balance = Bal
        self.Account_no =Acc

    def Debit(self,Amount):
        self.Balance -= Amount
        print(f"{Amount} was Debited.")
        print("Your Total Balance is ",self.Balance)

    def Creadit(self,Amount):
        self.Balance += Amount
        print(f"{Amount} has Creadited.")
        print("Your Total Balance is ",self.Balance)

Acc1 = Account(10000,987654321)
print(Acc1.Balance)
print(Acc1.Account_no)

Acc1.Debit(5000)
Acc1.Creadit(10000)

print("Thank You for Transaction")