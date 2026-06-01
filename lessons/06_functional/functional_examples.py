# optional parameter

'''def func(word, add=5, freq=1):
    return word*(freq+add)

call = func('tim',2,5)
print(call)'''

#static and class methods

'''class Person:

    population = 50
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def getPopulation(cls):
        return cls.population
    @staticmethod
    def isAdult(age):
        return age >= 18
    
    def display(self):
        return (self.name, 'is', self.age, 'years old')

    def __str__(self) -> str:
        return (f'Person: {self.name}, {self.age}')

newPerson = Person('İlker', 36)
print(newPerson.display())
# static mehtod sınıf içindeki ögeleri kullanmak yerine dışarıdan verilen parametrelerle mantıksal işlem yapıyor
print(newPerson.isAdult(36)) '''

#map func

'''li = [1,2,3,4,5,6,7,8,9,10]

def func(x):
    return x**x

# bunun yerine for loop ile de yapılabilir ama bu daha kolay
print(list(map(func, li)))

# list comprehention
print([func(x) for x in li]) '''

# Filter Func

'''def add7(x):
    return x+7

def isOdd(x):
    return x%2 !=0

a = [1,2,3,4,5,6,7,8,9,10]

#for loop yazmak yerine fonksiyon a listesindeki bütün elemanlar için uygulanıyor
b = list(filter(isOdd, a))
print(b)

# şimdi de map fonk ile b listesindeki bütün elemanları add7 fonksiyonundan geçirdik ve bütün elemanlara 7 eklendi
c = list(map(add7, b))
print(c)

# bütün bunlar uzun uzun for loop yazmak yerine tek satırda halledildi. 
'''

# lambda func (anonymous func)


# Normal Func
'''def func(x):
    return x+5

# print(func(2))

# x parametresi ve retun parametre + 5
func2 = lambda x: x+5 
# print(func2(2))

a = [1,2,3,4,5,6,7,8,9,10]

newlist = list(map(func, a))
print(f'New List Normal fun with Map {newlist}')

newlist = list(map(lambda x: x+5, a))
print(f'New List Lamda fun with Map {newlist}')'''

