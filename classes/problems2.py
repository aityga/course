# problem1
'''
class Factory:
    def __init__(self) -> None:
        pass
    def engine(self):
        return "Двигатель создан"
    def bridge(self):
        return "Ходовая часть создана"

class Toyota(Factory):

    def wheels(self):
        return "Колеса готовы"
    def windows(self):
        return "Стекла готовы"

fac = Toyota
t = [fac.engine("j"), fac.bridge("m"), fac.wheels("k"), fac.windows("k")]
print(t)
'''
# problem2
'''
class Zoo:
    
    def __init__(self):
        self.animal1 = 'tigr'
        self.animal2 = 'begemot'
        self.animal3 = 'jiraf'

zoo = Zoo()
zoo.animal1 = 'lev'
zoo.l = [zoo.animal2]
zoo.animal4 = zoo.l.append(zoo.animal3)
zoo.animal3 = 'zmeya'
print(zoo.animal1, zoo.animal3, zoo.l)
'''
# problem3
'''
class Student:
    name = 'vasya'
    lastname = 'ivanov'
    department = 'it'
    year_of_entrance = '2017'
    def __init__(self) -> None:
        pass
    def get_student_info(self):
        print(f"{self.name}{self.lastname} postupil v {self.year_of_entrance} g. na fakultet: {self.department}")
you = Student()
you.get_student_info()
'''