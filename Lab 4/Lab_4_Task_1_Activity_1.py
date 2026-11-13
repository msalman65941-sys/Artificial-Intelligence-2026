def mark_attendance(student):
    roll_no, name = student  # we assign student to roll no and name as a tuple
    attendance[roll_no] = name, "Present"  # dictionary to store attendance with roll number as key and name as value


attendance = {}
mark_attendance((101, "Salman"))
mark_attendance((102, "Shan"))
mark_attendance((103, "Sherry"))

print("Attendance:")
for roll_no in attendance:
    print(f"Roll No: {roll_no}, Name: {attendance[roll_no]}")
