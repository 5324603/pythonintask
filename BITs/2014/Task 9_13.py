#Задача №9 Вариант 13
#Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет"
#Martynov M.I.
#25.04.2016

import random
WORDS=("лес","кран","сложный","простой","машина","животные")
word=random.choice(WORDS)
live=5
bukva=""
slovo=""
(chislo)=len(word)
print("Я выбрал слово,угадай какое. В этом слове",str(chislo)," букв.")
print("У тебя "+str(live)+" попыток угадать буквы")
while live>0:
		#print (word)
		bukva=input("Введите букву\n")
		if bukva in list (word) :
			print("Да.")
			live=live-1
		else:
			print("Нет.")
			live=live-1
if live==0:
		slovo=input("Ваши попытки кончились\n")
if slovo==word:
			print("Вы угадали слово")
else:
			print("Вы не угадали слово")
input("Нажмите Enter для выхода")
