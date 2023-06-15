class Student:
    def __init__(self,name,mark):
        self.name=name
        self.mark=mark
    def getdetails(self):
        self.name=input("enter your name")
        self.mark=int(input("enter your mark"))
    def putdetails(self):
        print(self.name, self.mark)

class teacher(Student):
    def display(self):
        print("am derived class")

obj=teacher('','')
obj.getdetails()
obj.putdetails()
obj.display