# Напишите программу, которая принимает на вход координаты точки (X и Y),
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка.

x = int(input('Введите 1-е число: '))
y = int(input('Введите 2-е число: '))

if x>0 and y>0:
    print('Точка относится к четверти 1')
elif x<0 and y>0:
    print('Точка относится к четверти 2')
elif x<0 and y<0:
    print('Точка относится к четверти 3')
elif x>0 and y<0:
    print('Точка относится к четверти 4')