#Функциональный стиль программирования
#map() замена циклу for
lst=["1", "2", "3"]
int_lst=[]

for symbol in lst:
    int_lst.append(int(symbol))
print(lst)
print(int_lst)
#________________________________________________
gen_lst=[int(number) for number in lst]
print(gen_lst)
#_____________________________________________________
# 1. Создаем переменную
# 2. Вызов функции map() внутри переменной
# 3.

map_lst= map(int, lst)
print(list(map_lst))

names=["dior", "muhammad", "sanjar"]
map_names=map(str.capitalize, names)
print(names)
print(list(map_names))
lst=[23, 43, 55]
def double_number(number: int):
    return number**2
map_lst=map(double_number, lst)
print(lst)
print(list(map_lst))




filter()
words=["purple", "yellow", "orange", "apple", "nokia", "windows", "transformer"]
less_5=[]
more_5=[]


for word in words:
    if len(word)<=5:
        less_5.append(word)
    else:
        more_5.append(word)
print(less_5, more_5)

def get_wordsLessFive(word: str):
    return len(word)<=5
filter_lst= filter(get_wordsLessFive, words)
print(list(filter_lst))


words=["apple", "banana", "bmw", "aplk"]
def getWWA(word: str):
    return word.startswith("a")
def getWWB(word: str):
    return word.startswith("b")

filtereda=filter(getWWA, words)
print(list(filtereda))
filteredb=filter(getWWB, words)
print(list(filteredb))

#Git, GitHub












