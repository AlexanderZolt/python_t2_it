# Завдання 1
name=[]
score=[]
for i in range(int(input('enter number of students: '))):
    name.append(tuple(input('enter student name ').split()))
    score.append(list(map(int, input('enter score ').split())))
lib=dict(zip(name, score))
average={a[0]: sum(a[1])/len(a[1]) for a in lib.items()}
max_val = max(average.values())
min_val = min(average.values())
filtered_dict = {key: value for key, value in average.items() if value == max_val or value == min_val}
print("Best and worst studdent and their average score:", filtered_dict)

# Завдання 2
name=[]
group=[]
for i in range(int(input('enter number of students: '))):
    name.append(tuple(input('enter student name ').split()))
    group.append(input('enter groups ').split())
students=dict(zip(name, group))

print("Students in two or more groups: ", [student for student, groups in students.items() if len(groups) > 1])

print("Frontend students: ", [student for student, groups in students.items() if 'FrontEnd' not in groups])

print("Python or Java group students: ", [student for student, groups in students.items() if 'Python' in groups or 'Java' in groups])

#Завдання 3
measurements={
    'xxs':{'UA':42, 'DE': 36, 'US': 8, 'FR':38, 'GB':24},
    'xs':{'UA':44, 'DE': 38, 'US': 10, 'FR':40, 'GB':26},
    's':{'UA':46, 'DE': 40, 'US': 12, 'FR':42, 'GB':28},
    'm':{'UA':48, 'DE': 42, 'US': 14, 'FR':44, 'GB':30},
    'l':{'UA':50, 'DE': 44, 'US': 16, 'FR':46, 'GB':32},
    'xl':{'UA':52, 'DE': 46, 'US': 18, 'FR':48, 'GB':34},
    'xxl':{'UA':54, 'DE': 48, 'US': 20, 'FR':50, 'GB':36},
    'xxxl':{'UA':56, 'DE': 50, 'US': 22, 'FR':52, 'GB':38},
    } #Мені було ліньки писати повні назви, тому аліаси
def filtering(a,b): # Оскільки треба писати саме функцію...
    return(measurements[a][b])
measurement=input('enter measurements: ')
state=input('Enter state alias: ')
print(filtering(measurement, state))