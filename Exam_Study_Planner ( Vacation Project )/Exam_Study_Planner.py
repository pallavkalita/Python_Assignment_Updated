sub_list = []
sub_dict = {}
day_dict = {}
sub_time = {}
cmp_list = []

def add_sub(sub):
    sub_list.append(sub)
    
def display_sub():
    print(f"Incomplete subjects: {sub_list}.")
    print(f"Completed subjects: {cmp_list}.")
    print()

def display_actions():
    print()
    print("********************************************************")
    print()
    print("1. Add Subject")
    print("2. Delete Subject")
    print("3. Completed Subject")
    print("4. Display Subjects")
    print("5. Enter Study Time per Day")
    print("6. Exit")
    print()
    
    main()

def delete(sub_del):
    sub_list.pop(sub_del - 1)
    sub_dict.pop(sub_del)

def list_to_dict():
    for i in range(len(sub_list)):
        sub_dict[i + 1] = sub_list[i]

def time(study_time, count):
    per_subject_time = study_time // count
    print(f"Study time per subject: {per_subject_time} hours.")

def cmpltd(sub_cmp):
    n = sub_list.pop(sub_cmp - 1)
    cmp_list.append(n)
    sub_dict.pop(sub_cmp)
    
    print(f"Completed subjects are: {cmp_list}")
    print(f"Incomplete subjects are: {sub_list}")
    
    if len(sub_list) == 0:
        print()
        print(f"Hurray {name} ! You have completed your syllabus!")

    
def main():
    select = int(input("Select an action: "))
    
    if select == 1:
        n = int(input(">>>> Enter the number of subjects to add: "))
        print()
        
        for i in range(n):
            sub_number = len(sub_list) + 1
            sub = input(f"     >>>> Enter SUBJECT {sub_number}: ")
            add_sub(sub)
        
        global count
        count = len(sub_list)
        
        print()
        display_sub()
        print(f"Total subjects: {count}")
        print()
        
        display_actions()
        
    elif select == 2:
        sub_dict.clear()
        list_to_dict()
        sorted_dict = dict(sorted(sub_dict.items()))
        
        print(f"Subjects list: {sorted_dict}")
        print()
        sub_del = int(input("Enter subject number to delete: "))
        print()
        
        delete(sub_del)
        count = len(sub_list)
        
        print(f"Total subjects are: {count}")
        print()
        
        display_sub()
        display_actions()
        
    elif select == 3:
        sub_dict.clear()
        list_to_dict()
        sorted_dict = dict(sorted(sub_dict.items()))
        
        print(f"Subjects list: {sorted_dict}")
        print()
        sub_cmp = int(input("Enter completed subject number: "))
        print()
        
        cmpltd(sub_cmp)
        count = len(sub_list)
        
        print(f"Total subjects left: {count}")
        print()
        display_actions()
        
    elif select == 4:
        display_sub()
        display_actions()
        
    elif select == 5:
        study_time = int(input("Enter study time per day in hours: "))
        time(study_time, count)
        display_actions()
        
    elif select == 6:
        print("Bye, come again.")
        breakpoint()
        
    else:
        display_actions()

# *****************************************************************

global name
name = input("Enter your name: ")
print(f"\nHi {name}, welcome to Exam Study Planner\n")

print()
print("Hurray! You have completed your syllabus!")

display_actions()
