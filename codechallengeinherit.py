class Hospital:
    def __init__(self,admin,doctor,sister,department):
        self.admin=admin
        self.doctor=doctor
        self.sister=sister
        self.department=department


    def getdetails(self):
        self.admin=input("enter the admin")
        self.doctor=(input("enter the doctor name"))
        self.sister = (input("enter the sister name"))
        self.department = (input("enter the department"))

class Department:
    def display(self):
        print("ADMIN:",self.admin,"\nDOCTOR:", self.doctor,"\nSISTER" ,self.sister,"\nDEPARTMENT" ,self.department)

class patientward(Hospital,Department):
    def __init__(self, patientname, disease):
        self.patientname = patientname
        self.disease = disease

    def patientdetails(self):
        self.patientname=input("\n\nenter the patient name")
        self.disease=(input("enter the disease"))

    def show(self):
        print("PATIENT NAME",self.patientname, "\nDISEASE",self.disease)


obj=patientward('','')
obj.getdetails()
obj.display()
obj.patientdetails()
obj.show()





