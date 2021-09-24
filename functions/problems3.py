# problem1
'''
def add(a, b):
    sum = a + b
    return sum
print(add(3, 4))
def substract(a, b):
    diff = a - b
    return diff
print(substract(9, 4))
def multiply(a, b):
    multi = a * b
    return multi
print(multiply(10, 4))
def divide(a, b):
    div = a / b
    return div
print(divide(54, 4))
'''
# problem2
'''
def sentence(string):
    my_sentence = 0
    
    for i in string:
        my_sentence += 1
    return my_sentence
print(sentence("haha"))
'''
# problem3
'''
dict1 = {'e': 'q'}
dict2 = {'h': 'o'}
def pr3(dict1, dict2):
     dict1.update(dict2)
     return dict1
print(pr3(dict1, dict2))
'''
# problem4
'''
def menu():
    you = input("что кушать: ")
    with open('menu.txt', 'w') as file:
        f = file.write(you)
        return f
menu()
'''
# problem5
'''
user = input("Имя: ")
def file():
    f = open(f'/Users/aitegin/Desktop/course/functions/{user}.txt', 'w')
    f.close()
file()
'''
# problem01d
'''
def second():
    print("я вложенная функция")
    return second
def first():
    print("я главная функция")
    print(second())
    return first
print(first())
'''