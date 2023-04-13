a=[1,2,3,4,5]
#practice1
summ=0
for i in a:
    summ+=i
print(summ)

i=0
summ=0
try:
    while True:
        summ += a[i]
        i += 1
except IndexError:
    pass
print(summ)
#practice 2
import sys
try:
    with open(sys.argv[1], 'r') as f: print(f.read())
except FileNotFoundError: print("File not found")
finally: sys.exit(1)
#practice 3 - те ж саме, але навпаки
import sys
try:
    with open(sys.argv[1], 'r') as f: print(f.read()[::-1])
except FileNotFoundError: print("File not found")
finally: sys.exit(1)
#practice 4
banknotes=[1000, 500, 200, 100]
summ=int(input('enter summ of money: '))
if not summ%min(banknotes):
    for item in banknotes:
        amount=summ//item
        summ-=(item*amount)
        if amount:
            print (f'{item} - {amount} times')
        else: continue
else: print('money cannot be given')
#practice 5 - якщо передбачається відсутність банкнот номіналом 2,5,20,50,200,500, то задача виконується в лоб:
for banknote,amount in enumerate(input()[::-1]):
    print(f'{amount} of {10**banknote} banknotes')
# якщо ж такі купюри присутні, то у мене виходить незрозуміла фігня від якої поинає боліти голова.

# homework 1 and 2 in one file
"""оскільки мені ліньки створювати файл з числами ручками..."""
import random
with open('input.txt', 'w') as f:
    for i in range(20):
        line = ' '.join([str(random.randint(1, 99)) for _ in range(3)])
        f.write(line + '\n')
"""Перанальне виконання фізз-базза з конвертацією данних туди-сюди, друком і записом у новостворений файл"""
fizz = int(input("Enter fizz number: "))
buzz = int(input("Enter buzz number: "))

with open('input.txt', 'r') as input_file, open('result.txt', 'w') as output_file:
    for i in range(20):
        line = list(map(int, input_file.readline().split()))
        result_line = ' '.join(["FB" if i % fizz == 0 and i % buzz == 0 else "F" if i % fizz == 0 else "B" if i % buzz == 0 else str(i) for i in line])
        print(f'{" ".join(map(str, line))} --> {result_line}')
        output_file.write(f'{result_line.strip()} \n')