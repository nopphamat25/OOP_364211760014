"""
name: {Nopphamat Charornlap}
ID:{364211760014}
Group:{MIT221}
"""

#Class Relations - aggregation

class Teacher:
    def __init__(self,name):
        self.name = name

    def teacher_info(self):
        print(f'Teacher name:{self.name}')

class Faculty:
    #class attribute
    lst_teacher = list()

    def __init__(self,fac_name):
        self.fac_name =fac_name
    def fac_info(self):
        print(f'Faculty name:{self.fac_name} ')
    def add_teacher(self,teacher):
        self.lst_teacher.append(teacher)
    def teacher_info(self):
        print(f'Faculty name:{self.fac_name} has teacher following:')
        if len(self.lst_teacher) ==0:
            print("No teacher.")
        else:
            for x in self.lst_teacher:
                x.teacher_info()

#create object

t1 = Teacher("Puriwat")
t2 = Teacher("Phornprasert")

f1 = Faculty("MT")

t1.teacher_info()
f1.fac_info()

f1.add_teacher(t1)
f1.add_teacher(t2)
f1.teacher_info()

del f1

t1.teacher_info()
