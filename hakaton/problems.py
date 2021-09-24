# problem2
'''
s = input("word: ")
count_lower = 0
count_upper = 0
i = 0
while i < len(s):
    if s[i].islower(): count_lower += 1
    if s[i].isupper(): count_upper += 1
    i += 1
print(f"Заглавных букв {count_upper} , прописных букв {count_lower}")
'''
# problem4
'''
"Напишите функцию которая принимает в себя словарь где ключи это номера а значения страны.
Попросите пользователя ввести страну или ключ и выдайте ему результат."
d = {'1': 'kyrgyzstan', '2': 'kazahstan'}
def func():
    user = input()
    d = {"1": "kyrgyzstan", "2": "kazakhstan"}
    out = d.get(user)
    print(out)
func()
'''
# problem5
'''
fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1
print(fib(10))
'''
# problem6
'''
def fac(n):
    if n == 0:
        return 1
    return fac(n-1) * n

print(fac(n = int(input("factorial: "))))
'''
# problem7
'''
num = []
def convert(b):
    if (b == 0):
        return num
    num1 = b % 2
    num.append(num1)
    convert(b // 2)
a = int(input("number: "))
convert(a)
print("numeral system: ")
for i in num:
    print(i)
'''
# problem8
'''
def length(user):
    if not user:
        return 0
    return 1 + length(user[1:])
a = ['haha', 'lol', 'tr']
print("Длина списка равна: ")
print(length(a))
'''
