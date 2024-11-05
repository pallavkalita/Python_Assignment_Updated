patient = {}

def add_patient(Id , Name , Age , Disease):
    patient[Id] = {" Name " : Name,
                   " Age " : Age , 
                   " Disease " : Disease  }
    
def display_patient_info(Id):
    print(f"The patient details are : {patient[Id]}")
    
    
n = int(input("Enter number of patients : "))

for i in range(n):
    Id = input("Enter Id of patient : ")
    Name = input("Enter name of patient : ")
    Age = int(input("Enter age of patient : "))
    Disease = input("Enter disease of patient : ")
    add_patient(Id, Name, Age, Disease)
    print()
    

Id = input(" Enter Id of patient for display : ")
display_patient_info(Id) 