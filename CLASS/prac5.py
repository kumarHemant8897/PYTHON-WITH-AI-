from random import randint
class Train:

    def __init__(self,trainNo):
         self.trainNo=trainNo


    def book(self,fro,to):
        print(f"the ticket is booked in trian no:  {self.trainNo}, from {fro} to {to}")


    def getStaus(self):
        print(f"this trina number : {self.trainNo} is runnigg on time")


    def fare(self,fro,to):
          print(f"the ticket is booked in trian no:  {self.trainNo}, from {fro} to {to} is {randint(222,555)}")




t=Train(45666)
t.book("rampur","delhi")
t.getStaus()
t.fare("rampur","delhi")