# problem000 
'''
menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
print(menu)
menu.update({'besh_barmak': 130})
print(menu)
menu.update({'lagman': 135})
print(menu)
menu.pop('borsh')
print(menu)
'''

# problem10
'''
menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
print(menu)
menu.update({'drinks': ['coca-cola', 'sprite', 'fanta']})
print(menu)
'''

# problem020
'''
x = set()
x.add('.add("")')
x.add(".remove("")")
x.add(".difference("")")
x.add(".intersection_update()")
x.add(".clear()")
x.add('.discard("*")')
x.add(".pop()")
x.add('.update("*")')
x.add('.intersection("*")')
print(x)
'''

# problem31
'''
nnn = {}
for i in range(0, 3):
    name = input("Введите свое имя: ")
    passw = input("Введите свой пароль: ")
    nnn.update({name: passw})
print(nnn)
'''

# problem27
'''
x = {'alya': 'nurse', 'haha': 'teacher', 'jaja': 'player', 'koko': 'baller', 'lala': 'footballer'}
for i in x:
    print(f"Здравствуйте {i}. Прекрасная профессия {x[i]}")
'''
