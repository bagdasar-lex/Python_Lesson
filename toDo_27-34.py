#027 28

#num1 = float(input("Enter a float number: "))
#num1 = num1*2
#print(round(num1, 2))

#029
#import math
#print(round(math.pi, 5))

#030

#import math
#num = float(input("Enter number more than 500 "))
#num = math.sqrt(num)
#print(round(num, 2))

#031

#import math
#radius = float(input("Enter a radius of circle: "))
#area = math.pi*(radius**2)
#print(round(area, 4))
#height = float(input("Enter a height of cilinder: "))
#volume = area * height
#print(round(volume, 2))

#033

#num1 = int(input("Введите первое число: "))
#num2 = int(input("Введите второе число: "))
#answer1 = num1 // num2
#answer2 = num1 % num2
#print("Если разделить" , num1 , "на" , num2 , "получится " , answer1 , "с остатком" , answer2)

#34

#q = float(input(
#"""Вычилить площадь квадрата? Введите 1
#Вычислить площядь треугольника? Введите 2 """))
#if q == 1 :
#    sqSize = float(input("Введите сторону квадрата: "))
#    sArea = sqSize**2
#    print("Площадь квадрата ровна: " , sArea)
#elif q== 2 :
#    triSize1 = float(input("Введите длину стороны треугольна: "))
#    triSize2 = float(input("Введите высоту стороны треугольна: "))
#    triArea = (triSize1 * triSize2) / 2
#    print("Площадь треугольника ровна: " , triArea)
#else:
#    print("Ошибка ввода данных")


print(" 1) Вычилить площадь квадрата? Введите 1")
print(" 2) Вычислить площядь треугольника? Введите 2 ")
print()
selection = int(input("Введите 1 или 2 "))
