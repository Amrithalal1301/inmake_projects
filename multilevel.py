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

class parent(teacher):
    def newfun(self):
        print("am derived class2")

class admin(parent):
    def funadmin(self):
        print("am admin ")
obj=admin('','')
obj.getdetails()
obj.putdetails()
obj.display()
obj.newfun()
obj.funadmin()