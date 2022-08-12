class Employee():
    company = "Google"
    def getSalary(self):
        print(f"Salary Of Employee Working In {self.company} Is {self.salary}")
    def __init__(self,name,salary,subunits):
        self.name = name
        self.salary = salary
        self.subunits = subunits 
        print("Employee Is Created")

    def getDetails(self):
        print(f"Name Of Employee {self.name}")
        print(f"Salary Of Employee {self.salary}")
        print(f"Subunits Of Employee {self.subunits}")
        

jawad = Employee("Jawad",100,"Youtube")
jawad.getDetails()
