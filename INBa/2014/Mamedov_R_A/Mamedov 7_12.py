# Задача 7, Вариант 12 
# Разработайте систему начисления очков для задачи 6, в соответствии с которой игрок получал бы большее количество баллов за меньшее количество попыток.

# Мамедов Р.А.
# 30.03.2016

import random
print ('Отгадайте название одного из соборов Московского кремля ')
def get_random_sobor():
   sobors = ("Успенский собор","Архангельский собор","Благовещенский собор","Храм Положения ризы Божией Матери во Влахерне",
   "Колокольню Ивана Великого","Верхоспасский собор","Церковь Рождества Богородицы на Сенях",
   "Патриарший дворец и собор Двенадцати апостолов")
   return random.choice(sobors)
sobor = get_random_sobor()
user_sobor = input('Введите ваш вариант: ')
ball = 5
while sobor.lower() != user_sobor.lower() and ball >1:
    ball -= 2
    print('У вас остлось', ball, 'баллов', 'Попробуйте ещё раз')
    user_sobor = input('Введите ваш вариант: ')
if ball > 1:
   print("Да вы отгдали!"'У вас остлось', ball)
else:
    print('Баллы закончились, а вы не угадали собор ')
input ('Нажмите Enter для выхода')





