"""
name: {Nopphamat Charornlap}
ID:{364211760014}
Group:{MIT221}
"""

from EV_Car import EV_Car

#display
def display_evcar():
   if len(my_car) ==0:
       print("You had no car data.")
   else:
       print(f'You had {len(my_car)} following:')
       for x in my_car:
           x.display_evcar()
   print("\n")

# option
def display_option_system():
   select = 0
   print("Welcome to Car Data Store System (VDSS)")
   print("1. เพิ่มข้อมูล EV_Car")
   print("2. แสดงข้อมูล EV_Car")
   print("3. ออกจากระบบ")
   select = int(input("select(1-3)? : "))
   if select == 1:
       input_evcar_data()
   elif select == 2:
       display_evcar()
   elif select == 3:
       print("Thank You Love You Good Bye.")
       exit(0)
   else:
       print("Please, select number 1-3.")



# input data
def input_evcar_data():
   No = int(input("Enter Car No: "))
   Brand = input("Enter Car Brand: ")
   Model = input("Enter Car Model: ")
   Motor = int(input("Enter Car Motor: "))
   Horse_Power = int(input("Enter Car Horse Power: "))
   Battery_Size = float(input("Enter Car Battery Size(kWh): "))
   Range = int(input("Enter Car Range(km): "))
   Price = float(input("Enter Car Price: "))

   my_car.append(EV_Car(No,Brand,Model,Motor,Horse_Power,Battery_Size,Range,Price))
   print("\n-----------------------------------")
   print("Already add car to store.")
   print("-----------------------------------")

my_car = []
s = 0
while s == 0:
   display_option_system()










