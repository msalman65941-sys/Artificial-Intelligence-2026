all_students = ["Salman", "Ali", "Shan", "Sherry", "Ahmed"]

present_students = ["Salman", "Sherry", "Ahmed"]

all_set = set(all_students)
present_set = set(present_students)

absent_students = all_set - present_set

print("Absent Students:")

for student in absent_students:
    print(student)