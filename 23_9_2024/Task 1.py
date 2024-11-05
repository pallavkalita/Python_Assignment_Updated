student_list = []

def add_student_det(student_details):
    student_list.append(student_details)

def student_det(i, Id, Name, Grade):
    student_details = {}
    student_details[f"Id_st{i+1}"] = Id
    student_details[f"Name_st{i+1}"] = Name
    student_details[f"Grade_st{i+1}"] = Grade
    return student_details

def check_duplicate_id(Id):
    for student in student_list:
        for key in student:  
            if student[key] == Id:
                return True
    return False

n = int(input("Enter number of students: "))
print("Enter details of Students")

for i in range(n):
    Id = input("Enter Id: ")
    
    if check_duplicate_id(Id):
        print("Cannot enter duplicate ID")
        continue

    Name = input("Enter Name: ")
    Grade = input("Enter Grade: ")
    
    student_details = student_det(i, Id, Name, Grade)
    add_student_det(student_details)

print("\nList of Students:")
for i in range(len(student_list)):
    print(f"Student{i+1} = {student_list[i]}")
