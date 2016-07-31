#test class
class Person:
    '''Represent a person'''
    population=0

    def __init__(self,name):
        '''initialize one's data'''
        self.name=name
        Person.population+=1
    def __del__(self):
        '''die'''
        Person.population-=1
        print("Go Die!")
    def sayHi(self):
        print("Hi!I'm",self.name)
        print(Person.population)
class student(Person):
    '''Represent a student'''
    def __init__(self,name,score=0):
        '''initialize one's score'''
        Person.__init__(self,name)
        self.score=score
    def tell(self):
        print(self.name,self.score)
    def __del__(self):
        print('Nothing')

p=Person("Yang")
p.sayHi()
q=Person("Master")
q.sayHi()
del p
q.sayHi()
p=student("Li",10)
p.tell()
p.sayHi()
