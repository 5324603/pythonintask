#Задача №7 Вариант 13
#Создайте игру, в которой компьютер загадывает название одного из двух спутников Марса, а игрок должен его угадать.
#Martynov M.I.
#21.04.2016
 
 
import random
sputniki=("Деймос","Фобос")
sputn=random.randint(0,1)
Ball=100
rand=sputniki[sputn]
print("Я загадал название одного из спутников марса")
print("У Вас есть 100 баллов ,чтобы отгадать")
#print(rand)
otvet=0
while(otvet)!=(rand):
      otvet=input("Введите назмание спутника:")
      if(otvet)!=(rand):
            print("Вы не угадали,попробуйте снова.При этом вы потеряли 15 баллов")
            Ball-=15
      elif(otvet)==(rand):
               print("Вы угадали.")
               print("Ваши баллы:"+str(Ball))
               break
input("Нажмите Enter для выхода.")	
