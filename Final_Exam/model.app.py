"""
name: {Nopphamat Charornlap}
ID:{364211760014}
Group:{MIT221}
"""

#from model import Person,Student,Employee,Devices,Mobile,Tablet,Labtop,Device_Report

def display_option_system():
  select = 0
  print("Welcome to Data Store System")
  print("1.Add user")
  print("2.Add device for user")
  print("3.Delete device for user")
  print("4.Display device information")
  print("5.Exit")
  select = int(input("select(1-5)? : "))
  if select == 1:
      input_person()
  elif select == 2:
      add_device()
  elif select == 3:
      delete_device()
  elif select == 4:
      display_device()
  elif select == 5:
      print("Good Bye.")
      exit(0)
  else:
      print("Please, select number 1-5.")

def input_person():
 name = input('Name: ')
 age = int(input('Age: '))
 email = input('Email: ')
 return name,age,email

def input_student():
 sid = input('Student ID: ')
 major = input('Major: ')
 return sid,major

def input_employee():
 eid = input('Employee ID: ')
 position = input('Position: ')
 return eid,position

if __name__ == '__main__':
 print('Enter your information: ')
 p = input_person()

 x = input('Are you Student(s) or Employee(e) :: (s/e): ?')
 if x.lower() == 's':
     s = input_student()
 else:
     position = input_employee()

def add_device():
   brand = input('Brand: ')
   model = input('Model: ')
   price = float(input('Price: '))
   return brand, model, price

#def delete_device():
#def display_device():

s = 0
while s == 0:
  display_option_system()














