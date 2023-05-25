def spam(number):
        return 'bulochka'*number

def my_sum(list_of_numbers):
    a=0
    for i in list_of_numbers:
       a+=i
    return a

def shortener(string):
    b=string.split()
    for i,j in enumerate(b):
        if len(j)>6:
            b[i]=j[:6]+'*'
    return ' '.join(b)

def compare_ends(words):
    counter=0
    for i in words:
        if len(i)>=2 and i[0]==i[-1]:
            counter+=1
    return counter

