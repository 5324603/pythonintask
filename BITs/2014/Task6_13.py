#Задача №6 Вариант 13
#Создайте игру, в которой компьютер загадывает название одного из двух спутников Марса, а игрок должен его угадать.
#Martynov M.I.
#21.04.2016
 
 
import random
sputniki=("Деймос","Фобос")
sputn=random.randint(0,1)
rand=sputniki[sputn]
print("Я загадал название одного из спутников марса")
#print(rand)
otvet=0 
while(otvet)!=(rand):
    otvet=input("Введите назмание спутника:")
    if(otvet)!=(rand):
        print("Вы не угадали,попробуйте снова.")
    elif(otvet)==(rand):
        print("Вы угадали.")
        break
input("Нажмите Enter для выхода")	
