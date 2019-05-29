# Вывести последнюю букву в слове
word = 'Архангельск'
# ???
r = list(word)
print(r[-1])

# Вывести количество букв а в слове
word = 'Архангельск'
# ???
q = word.lower()
print(q.count('а'))

# Вывести количество гласных букв в слове
word = 'Архангельск'
# ???
vow = 0
cons = 0
for i in word:
    letter = i.lower()
    if letter == "й" or letter == "у" or letter == "e" or letter == "э" or letter == "ы" or letter == "а" or letter == "о" or letter == "я" or letter == "и" or letter == "ю":
        vow += 1
    else:
        cons += 1
print("Vowels %i\nConsonants %i" % (vow, cons))

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
# ???
print(len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
# ???
t = sentence.split()
print(t)
for x in t:
    print(x[0])

# Вывести усреднённую длину слова.
sentence = 'Мы приехали в гости'
# ???
v = sum(len(t) for word in t)/len(t)
print(v)
