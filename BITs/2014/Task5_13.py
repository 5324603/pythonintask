#Задача №5 Вариант 13
#Гадание апостолов
#Martynov M.I.
#21.04.2016
 
 
import random
print("один из апостолов")
apostol1=("Андрей")
apostol2=("Пётр")
apostol3=("Иоанн")
apostol4=("Иаков Зеведеев ")
apostol5=("Филипп")
apostol6=("Варфоломей ")
apostol7=("Матфей,")
apostol8=("Фома")
apostol9=("Иаков Алфеев")
apostol10=("Фаддей ")
apostol11=("Симон Кананит")
apostol12=("Иуда")
apostols=random.randint(1,12)
if apostols==1:
   print(apostol1)
if apostols==2:
   print(apostol2)
if apostols==3:
   print(apostol3)
if apostols==4:
   print(apostol4)
if apostols==5:
   print(apostol5)
if apostols==6:
   print(apostol6)
if apostols==7:
   print(apostol7)
if apostols==8:
   print(apostol8)
if apostols==9:
   print(apostol9)
if apostols==10:
   print(apostol10)
if apostols==11:
   print(apostol11)
elif apostols==12:
   print(apostol12)
   
input("Нажмите Enter для выхода")
