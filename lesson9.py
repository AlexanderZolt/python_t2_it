#Задача 1
from math import ceil
flatnumber, flatsonstore, stores= list(map(int, input().split()))
def address():
    storeys=int(ceil(flatnumber/flatsonstore))
    entry=int(ceil(storeys/stores))
    store=storeys-((entry-1)*stores)
    return (entry,store)
print(address())
# Задача 2
diamond=int(input('enter number of stars: '))
if diamond>0 and diamond%2:
    a=['*'*i for i in range(1, diamond+1, 2)]
    b=['*'*i for i in range(diamond, 0, -2)]
    c=a+b[1:]
    for i in c:
        print(i.center(diamond))
# Задача 3
from sys import argv
with open(argv[1], 'r') as input_file:
    for _ in input_file:
        line=_.split(';')
        line1=list(map(int, line[0].split()))
        line2=list(map(int, line[1].split()))
        print(line, sum(line1)//len(line1)==line2[0] and sum(line1)%len(line1)==line2[1])
    
