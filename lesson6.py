#Практичне завдання 1 вирівняти текст по розміру і вивести обидва варіанта
def to_lower_case(s):
    return s.lower()

def to_upper_case(s):
    return s.upper()

listing = ["HeLLo", "wOrLD", "PyThOn"]
print("Lowercase strings:", list(map(to_lower_case, listing)))
print("Uppercase strings:", list(map(to_upper_case, listing)))
#Практичне завдання 2 - вивести квадрати простих чисел у проміжку від 0 до 50
def square_num(num):
    return num**2

def is_prime(num):
    if num <= 2: # один і два - теж прості числа, але про це забувають
        return True
    for i in range(2, int(num/2)+1):
        if num%i == 0:
            return False
    return True

primes = list(filter(is_prime, (range(51))))
print(primes)
print(list(map(square_num, primes)))
#Практичне завдання 3. Вивести статистику появи слів у текстовому файлі
def count_words(filename):
    # створили словник для слів
    word_counts = {}
    #читаємо файл і одразу перетворюємо текст з нього у список
    with open(filename, 'r') as f:
        words = f.read().split()
    #рахуємо слова у сипску і додаємо до словника два значення: ключ у вигляді слова та значення - його кількість
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    #Впорядковую словник по ключам по алфавіту і перетворюю його у список кортежів
    word_counts=sorted(word_counts.items(), key=lambda x: x[0])
    return [(word, count) for word, count in word_counts]

print(count_words('sample.txt'), sep='\n')
  
#Домашнє завдання: написати свій власний zip.
def mein_zip(a, b):
    min_len = min(len(a), len(b))
    if not min_len:# перевірка на ідіота і встановлюємо менший зі списків
        return "Error between seat and keyboard - add two lists, not one"
    else:
        zipped = []
        for i in range(min_len): #Перебираємо паралельні списки і збираємо їх елементи у кортежі
            tup = tuple([a[i], b[i]])
            zipped.append(tup)
        return zipped

list1=['a','b','c']
list2=['z','x','y']
list3=[]
print(mein_zip(list1,list2)) #Нормальний випадок
print(mein_zip(list2,list3)) #Ідіотський випадок
#