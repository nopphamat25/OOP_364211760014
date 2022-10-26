"""
name: {Nopphamat Charornlap}
ID:{364211760014}
Group:{MIT221}
"""


class Person:
    def __init__(self, name, age, email):
        # object attributes
        self.__name = name
        self.__age = age
        self.__email = email

    def __str__(self):
        print(f'Name: {self.__name} '
              f' Age: {self.__age} '
              f' email: {self.__email} ')

    # getter and setter method
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        self.__age = age

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email


class Student(Person):
    def __init__(self, name, age, email, sid, major):
        super().__init__(name, age, email)
        self.__sid = sid
        self.__major = major

    def __str__(self):
        print(f' Student Id: {self.__sid} '
              f' Major: {self.__major} ')

    # getter and setter
    def get_sid(self):
        return self.__sid

    def set_sid(self, sid):
        self.__sid = sid

    def get_major(self):
        return self.__major

    def set_major(self, major):
        self.__major = major


class Employee(Person):
    def __init__(self, name, age, email, eid, position):
        super().__init__(name, age, email)
        self.__sid = eid
        self.__major = position

    def __str__(self):
        print(f' Employee Id: {self.__eid} '
              f' Position: {self.__position} ')

    # getter and setter
    def get_eid(self):
        return self.__eid

    def set_eid(self, eid):
        self.__eid = eid

    def get_position(self):
        return self.__position

    def set_position(self, position):
        self.__position = position


class Devices:
    my_device = []

    def __init__(self, brand, model, price):
        # object attributes
        self.__brand = brand
        self.__model = model
        self.__price = price

    def device_info(self):
        print(f' Brand: {self.__brand} '
              f' Model: {self.__model} '
              f' Price: {self.__price}')

    # getter and setter method
    def get_brand(self):
        return self.__brand

    def set_brand(self, brand):
        self.__brand = brand

    def get_model(self):
        return self.__model

    def set_model(self, model):
        self.__model = model

    def get_price(self):
        return self.__price

    def set_price(self, price):
        self.__price = price


class Mobile(Devices):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)

    def __str__(self):
        print(f' Mobile Brand: {self.__brand} '
              f' Model: {self.__model} '
              f' Price: {self.__price} ')


class Tablet(Devices):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)

    def __str__(self):
        print(f' Tablet Brand: {self.__brand} '
              f' Model: {self.__model} '
              f' Price: {self.__price} ')


class Laptop(Devices):
    def __init__(self, brand, model, price):
        super().__init__(brand, model, price)

    def __str__(self):
        print(f' Laptop Brand: {self.__brand} '
              f' Model: {self.__model} '
              f' Price: {self.__price} ')


class Devices_Report:
    def __init__(self, owner):
        self.owner = owner
        self.device_list = list()

    def device_report_info(self):
        print(f'Devices_Report: ')
        self.owner.__str__()
        c = 1
        if len(self.device_list) == 0:
            print(f'  No device data.')
        else:
            for x in range(len(self.device_list)):
                print(f'{c}. {self.device_list[x].get_name()}')
                c += 1

    def add_device(self, Devices):
        self.device_list.append(Devices)


    def delete_device():
       print("Which one do yo want to remove?")
       device_info()
       n = len(my_device)
       s = 1
       while s:
           s = int(input(f'select(1--{n}) or type 0 to main options: '))
           if s in range(1, n + 1):
               my_device.pop(s - 1)
               print(" Already delete laptop data. ")
               break
           elif s == 0:
               break
           else:
               print(f'Please, select number 1-{n} or or type 0 to main options.')


