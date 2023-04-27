import random
# open the file for writing
with open('input.txt', 'w') as f:
    # generate 20 strings of three random two-digit numbers separated by spaces
    for i in range(20):
        line = ' '.join([str(random.randint(1, 99)) for _ in range(3)])
        # write the line to the file and add a newline character
        f.write(line + '\n')
