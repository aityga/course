# problem1
'''
user = input("Имя: ")
def file():
    f = open(f'{user}.txt', 'w')
    f.write('tyu')
    f.close()
file()
'''
# problem2
'''
import random
def gen_number():
    ber = [1, 4, 5, 7, 9, 0]
    nums = random.sample(ber, k = 6)
    print("0444", nums)
gen_number()
'''
# problem0102
'''
you = int(input("Money: "))
print(you)

def notes(a):
    banknotes = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 3, 1]
    x = 0
    for i in range(12):
        q = banknotes[i]
        x += int(a / q)
        a = int(a % q)
    if a > 0:
        x = -1
    return x
print(notes(you))
'''
# problem0103
'''
def multi(a, b):
    ply = a * b
    return ply
print(multi(3, 6))

def divide(c, d):
    div = c / d
    return div
print(divide(15, 5))

def sum():
    m = multi(3, 6)
    d = divide(15, 5)
    print(m + d)
sum()
'''

