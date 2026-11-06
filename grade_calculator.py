student_name = "Rahim"

print(f"Enter student name: {student_name}")

math_mark = 85
print(f"Math mark: {math_mark}")

English_marks = 75
print(f"English mark: {English_marks}")

Python_marks = 90
print(f"Python mark: {Python_marks}")

print(f"student name: {student_name}")

average_marks = (math_mark + English_marks + Python_marks) / 3
print(f"Average marks: {average_marks}")



if 80 <= average_marks <= 100:
    print("A+")
elif 70 <= average_marks < 80:
    print("A")
elif 60 <= average_marks < 70:
    print("A-")
elif 50 <= average_marks < 60:
    print("B")
elif 40 <= average_marks < 50:
    print("C")
else: 
    print("F")