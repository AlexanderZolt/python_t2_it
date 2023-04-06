#task 1 bytewise
print("odd" if int(input()) & 1 else "even")
#task 2
x=int(input())
if x&1 and (x//3 and x//5) and x%10:#odd numbers cannot be divided by 10
    print('conditions met')
else: print('conditions not met')
#task 3
y=int(input())
print(', '.join([str(i) for i in range(2, y//2+1) if not y%i]))    
#task 4
for x,y in enumerate(input()[::-1]):
    print(f'{y}, 10**{x}')
#task fizz-buzz
fizz = int(input("Enter fizz: "))
buzz = int(input("Enter buzz: "))
limit = int(input("Enter limit: "))
result = ["FB" if i % fizz == 0 and i % buzz == 0 else "F" if i % fizz == 0 else "B" if i % buzz == 0 else i for i in range(1, limit+1)]
print(*result, sep=" ")