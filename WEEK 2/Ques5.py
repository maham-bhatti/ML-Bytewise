
student = []

for i in range(3):
    print('Student', i + 1, 'details')
    name = input('Enter the name of the student: ')
    age = input('Enter the age of the student: ')
    grade = input('Enter the grade of the student: ')
    student.append((name, age, grade))

stud_dic = {name: (age, grade) for name, age, grade in student}

print('\nStudent details are:')
for name, (age, grade) in stud_dic.items():
    print('Name:', name, 'Age:', age, 'Grade:', grade)
