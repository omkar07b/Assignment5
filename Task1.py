Student = {'Alice':85,'Omkar':75,'XYZ':65}

a = input("Enter the student's name:")

if a in Student:
    print("Alice's marks:",Student[a])
else:
    print("Student not found.")