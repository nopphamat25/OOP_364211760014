"""
Name: {Nopphamat Charoenlap}
SID: {364211760014}
Group: {MIT221}
"""

"""
เขียนโปรแกรมไพธอนเพื่อนำเลขบัตรประชาชนมาบวกกันเพื่อทำนายดวงชะตาดังนี้
• สร้างฟังก์ชันเพื่อหาผลรวมของเลขบัตรประชาชน โดยใช้ชื่อฟังก์ชั่นว่า sumPID()
• สร้างฟังชั่นชื่อ getFortune() เพื่อทำนายดวงชะตา ถ้าเป็นเลขคู่ให้ทำนายว่า your fortune is good
• ถ้าเป็นเลขคี่ ให้ทำนายว่า your fortune is very good

ใช้ฟังก์ชั่น split()
"""

def getPTD():
    sumPID = [int(x) for x in input(f'เลขบัตรประชาชน : ')]
    return sumPID

def getFortune(*var):
    resultlist = []
    for x in var:
        if x % 2 == 0:
            resultlist.append('Your fortune is good')
        else:
            resultlist.append('Your fortune is very good')
    return resultlist

PID = getPTD()
print(f'ผลรวมเลขบัตรประชาชน : {sum(PID)}')
print(f'ผลการทำนายของคุณ : {getFortune(sum(PID))}')

