class bank:
    def __init__(self,cno,pin):
        self.cno = cno
        self.pin = pin

    def checkBalance(self):
        print("Balance : You are broke")
    
    def Withdrawal(self,amount):
         print("Withdrawal : you have no money")

def main():
    n = bank(10,20)
    n.checkBalance()
    n.Withdrawal(100)

main()


        

        