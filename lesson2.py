# задание 1 - условные операторы

def different_age(age):
    list_work = ["работа","институт","школа","садик"]
    list_age = [20,16,6,1]
    for i in range(len(list_age)):
        if age>list_age[i]:
            return list_work[i]
             
age = int(input())
result = different_age(age)
print(result) 

# задание 2 - условные операторы

def string(str1,str2):
    list_values = [not isinstance(str1,str) or not isinstance(str2,str), str1 is str2, len(str(str1))>len(str(str2)), str2=="python"]
    for i in range(len(list_values)):
        if list_values[i]:
            return i
    

# задание 1 - цикл for

d=list(range(10))
print(*d)

# задание 2 - цикл for

string = input()
for i in string:
    print(i)

# задание 3 - цикл for

statistics = [{'school_class': '4a', 'scores': [3,4,4,5,2]}, {'school_class': '4b', 'scores':[5,5,4,3,4]}]
summa, len_s = 0, 0 
for i in statistics:
    print(f'Класс {i["school_class"]} средний бал {sum(i["scores"])/len(i["scores"])}')
    summa += sum(i["scores"])
    len_s += len(i["scores"])
print(f'Средний бал по школе {summa/len_s}')

# задание 1 - цикл while

def hello_user(x=None):
    while x != "хорошо":
        x = input()

hello_user()

# задание 2 - цикл while

def ask_user(x=None):
    ask = {"как дела":"хорошо", "что делаешь":"занимаюсь", "какой сегодня день":"чудесный"}
    while x!="пока":
        x = input("Спроси меня").lower().strip()
        print(ask.get(x,"у меня нет ответа на твой вопрос"))
    print("Пока")

ask_user()

# задание 1 - исключения

def hello_user(x=None):
    while x != "хорошо":
        try:
            x = input()
        except KeyboardInterrupt:
            print("Пока")
            break   

hello_user()

# задание 2 - исключения

def discounted(price, discount,max_discount=20):
    try:
        price = abs(float(price))
        discount = abs(float(discount))
        max_discount = abs(int(max_discount))
    except ValueError:
        return "Неверное значение аргумента"
    except TypeError:
        return "Неверный тип аргумента"
    if discount >= 100:
        price_with_discount = price
    else:
        price_with_discount = price - (price * discount / 100)
    return price_with_discount

print(discounted(100,[]))




