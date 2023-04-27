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
# fizz = int(input("Enter fizz number: "))
# buzz = int(input("Enter buzz number: "))

# with open('input.txt', 'r') as input_file, open('result.txt', 'w') as output_file:
#     for i in range(20):
#         line = input_file.readline().strip().split()
#         result_line = ''
#         for number in line:
#             if int(number) % fizz == 0 and int(number) % buzz == 0:
#                 result_line += 'FB '
#             elif int(number) % fizz == 0:
#                 result_line += 'F '
#             elif int(number) % buzz == 0:
#                 result_line += 'B '
#             else:
#                 result_line += number + ' '
#         print(f'{" ".join(line)} --> {result_line}')
#         output_file.write(result_line.strip() + '\n')

# with open('input.txt', 'r') as input_file, open('result.txt', 'w') as output_file:
#     for i in range(20):
#         line = list(map(int, input_file.readline().split()))
#         result_line = ' '.join(["FB" if i % fizz == 0 and i % buzz == 0 else "F" if i % fizz == 0 else "B" if i % buzz == 0 else str(i) for i in line])
#         print(f'{" ".join(map(str, line))} --> {result_line}')
#         output_file.write(f'{result_line.strip()} \n')