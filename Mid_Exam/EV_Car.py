"""
name: {Nopphamat Charornlap}
ID:{364211760014}
Group:{MIT221}
"""

class EV_Car:
   #class attribute
   my_car = []

   def __init__(self,No,Brand,Model,Motor,Horse_Power,Battery_Size,Range,Price):
       self.No = No
       self.Brand = Brand
       self.Model = Model
       self.Motor = Motor
       self.Horse_Power = Horse_Power
       self.Battery_Size = Battery_Size
       self.Range = Range
       self.Price = Price
       self.my_car.append(self)

   def display_evcar(self):
       print(f'No:{self.No} '
             f'Brand:{self.Brand} '
             f'Model:{self.Model} '
             f'Motor:{self.Motor} '
             f'Horse_Power:{self.Horse_Power} '
             f'Battery_Size:{self.Battery_Size} '
             f'Range:{self.Range} '
             f'Price:{self.Price}')

