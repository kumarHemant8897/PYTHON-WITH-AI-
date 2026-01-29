from random import randint
class Train:

    def __init__(slf,trainNo):
         slf.trainNo=trainNo


    def book(slf,fro,to):
        print(f"the ticket is booked in trian no:  {slf.trainNo}, from {fro} to {to}")


    def getStaus(slf):
        print(f"this trina number : {slf.trainNo} is runnigg on time")


    def fare(slf,fro,to):
          print(f"the ticket is booked in trian no:  {slf.trainNo}, from {fro} to {to} is {randint(222,555)}")




t=Train(45666)
t.book("rampur","delhi")
t.getStaus()
t.fare("rampur","delhi")