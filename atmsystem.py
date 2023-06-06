class Atm:
    def __init__(self):
        self.pin=''
        self.balance=0
        self.menu()
        
    def menu(self):
        print("enter language you want")
        selection=int(input("""
          1.create your pin.
          2.change your pin.
          3.check balance.
          4.withdraw balance
          5.exit from system
        
        """))
        if selection==1:
            self.createpin()
        elif selection==2:
            self.changepin()
        elif selection==3:
            self.checkbalance()
        elif selection==4:
            self.withdraw()
        else:
            print("this is not fare")
            exit()
    def createpin(self):
        pin1=int(input("enter your previous pin"))
        if len(pin1)<4:
            print("the length must be 4")
            self.createpin()
        else:
            newpin=pin1
            print("your pin is long enough",newpin)
            self.menu()
    def changepin(self):
        if self.newpin==input("enter previous pin"):
               self.newpin=input("enter current pin")
               print("the new pin is created")
        else:
               print("you enter wrong pin ") 
        self.menu()
    def checkbalance(self):
        newpin1=input("enter your pin") 
        if self.pin==newpin1:
            print("your balance is",self.balance)           
        else:
            print("incorrect pin")
        self.menu()
    
s1=Atm()