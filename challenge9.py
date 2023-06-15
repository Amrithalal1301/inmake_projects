class Computer:
    def __init__(self, ram,  processor):
        self.ram = ram
        self.processor = processor

    def getspecs(self):
        print("Enter specifications")
        self.ram = input("Enter RAM size: ")
        self.processor = input("Enter PROCESSOR model: ")

    def displayspecs(self):
        print("Ram size:{}  Processor:{}".format(self.ram, self.processor))


class Desktop(Computer):
    def __init__(self, casecolor):
        self.casecolor = casecolor

    def get_case_color(self):
        self.casecolor = input("Enter case color: ")

    def show_case_color(self):
        print("Case color:{}".format(self.casecolor))


class Laptop(Computer):
    def __init__(self, weight):
        self.weight = weight

    def get_weight(self):
        self.weight = input("Enter weight: ")

    def show_weight(self):
        print("Laptop weight:{}".format(self.weight))


object1 = Laptop("")
print("specifications for Laptop")
object1.getspecs()
object1.get_weight()
object1.displayspecs()
object1.show_weight()

object2 = Desktop("")
print("\nspecifications for Desktop")
object2.getspecs()
object2.get_case_color()
object2.displayspecs()
object2.show_case_color()


