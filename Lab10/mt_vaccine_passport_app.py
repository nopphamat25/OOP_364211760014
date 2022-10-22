"""
name: {Nopphamat Charornlap}
ID:{364211760014}
Group:{MIT221}
"""

from model import Person,Student,Vaccine,Vaccine_Passprot

p1 = Person("Nopphamat",22,50.0,161)

v1 = Vaccine("Astrazeneca")
d1 = "10/7/2565"

vp1 = Vaccine_Passprot(p1)

vp1.vaccine_passport_info()

vp1.add_vaccine(v1)
vp1.add_date(d1)
vp1.vaccine_passport_info()

v2 = Vaccine("Sinovac")
d2 = "10/8/2565"

vp1.add_vaccine(v2)
vp1.add_date(d2)

vp1.vaccine_passport_info()

#Student
s1 = Student("Phornprasert",38,75,165,"MIT")

v3 = Vaccine("Sinopharm")
d3 = "11/8/2565"

vp2 = Vaccine_Passprot(s1)
vp2.add_vaccine(v3)
vp2.add_date(d3)

vp2.vaccine_passport_info()

