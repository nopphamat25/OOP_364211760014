"""
name: {Nopphamat Charornlap}
ID:{364211760014}
Group:{MIT221}
"""

#polymrphism - การพ้องรูป

#function polymrphism
l ={1,2,3,4,5}
x = 100
print(l)
print(x)
s = "RUTS"
print(len(l))
print(len(s),s[2])

#polymrphism with class method
class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info (selt):
        print(f'I am a cat,my name is {selt.name}'
              f'I am {selt.age} years old.')

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(selt):
        print(f'I am a dog,my name is {selt.name}'
              f'I am {selt.age} years old.')

#create object

c = Cat("mumu",2)
d = Dog("luulu",5)

animal = [c,d]
for x in animal:
    x.info()