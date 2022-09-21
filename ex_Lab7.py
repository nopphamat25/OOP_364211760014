"""
name: {Nopphamat Charornlap}
ID:{364211760014}
Group:{MIT221}
"""

class Labtop:
    def __init__(self,Brand,Model,CPU,RAM ,Display,Storage,Price):
        self.__Brand = Brand
        self.__Model = Model
        self.__CPU = CPU
        self.__RAM = RAM
        self.__Display = Display
        self.__Storage = Storage
        self.__Price = Price

   # getter and setter

    def get_Brand(self):
        return self.__Brand
    def set_Brand(self, Brand):
        self.__Brand = Brand

    def get_Model(self):
        return self.__Model
    def set_Model(self, Model):
        self.__Model = Model

    def get_CPU(self):
        return self.__CPU
    def set_CPU(self, CPU):
        self.__CPU = CPU

    def get_RAM(self):
        return self.__RAM
    def set_RAM(self, RAM):
        self.__RAM = RAM

    def get_Display(self):
        return self.__Display
    def set_Display(self, Display):
        self.__Display= Display

    def get_Storage(self):
        return self.__Storage
    def set_Storage(self, Storage):
        self.__Storage = Storage

    def get_Price(self):
        return self.__Price
    def set_Price(self, Price):
        self.__Price = Price

    def __str__(self):
        print(f'Brand:{self.__Brand}'
              f' Model:{self.__Model} '
              f'CPU:{self.__CPU}'
              f' RAM:{self.__RAM}'
              f'Display:{self.__Display} '
              f'Storagel:{self.__Storage} '
              f'Price:{self.__Price}')

Lad = Labtop ("ASUS","Vivobook 15x","lntel Core i5-12500H",8,15.6,512,27990)
Lad.__str__()
print(Lad.get_Brand())

Lad.set_Brand("Lenovo")
print(Lad.get_Brand())

print(Lad.get_Model())

Lad.set_Model("Vivobook")
print(Lad.get_Model())
