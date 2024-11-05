grades = [('Ram', 90), ('Rohan', 85), ('Ray', 88)]

def calculate_average(grades):
    total = sum(grade for _, grade in grades)
    average = total / len(grades)
    highest_grade = max(grade for _, grade in grades)
    lowest_grade = min(grade for _, grade in grades)
    
    # Find the names of the students with the highest and lowest grades
    highest_students = [name for name, grade in grades if grade == highest_grade]
    lowest_students = [name for name, grade in grades if grade == lowest_grade]

    print(f"Average Grade: {average:.2f}")
    print(f"Highest Grade: {highest_grade} by {', '.join(highest_students)}")
    print(f"Lowest Grade: {lowest_grade} by {', '.join(lowest_students)}")

    return average, highest_grade, lowest_grade


calculate_average(grades)
