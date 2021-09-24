# problem1
'''
list = ['name', 'age', '1', '19']
print(list)

def viceversa():
    list.reverse()
    print(list)

viceversa()
'''
# problem2
'''
def fibonacci():
    a = 0
    b = 1
    count = 10
    c = 0
    while c < count:
        print(a)
        n = a + b
        a = b
        b = n
        c += 1
fibonacci()
'''
#  problem3
'''
def plus():
    a = int(input("num1: "))
    b = int(input("num2: "))
    sum = a + b
    print(sum)


def minus():
    c = int(input("num3: "))
    d = int(input("num4: "))
    diff = c - d
    print(diff)


def together():
    plus()
    minus()
together()
'''