# Напишіть скрипт, який обчислює площу прямокутника a*b, площу
# трикутника 0.5*h*a, площу кола pi*r**2 і цей скрипт використати в іншому
# модулі, в якому ми запитуємо користувача площу якої фігури він хоче
# обчислити.
# (для виконання завдання необхідно імпортувати модуль math, а з нього
# функцію pow() та значення змінної пі, модуль1, який містить три функції для
# знаходження площ, модуль2, в якому імпортований модуль1 і виконується
# основна логіка програми).

from math import pi 
from math import pow

def area_rectangle(length_rectangle, breadth_rectangle):
    """ This function returns the area of a rectangle """
    return f'Area of a rectangle - {length_rectangle * breadth_rectangle}'

def area_triangle(base_triangle, height_triangle):
    """ This function returns the area of a triangle """
    return f'Area of a triangle - {1/2 * base_triangle * height_triangle}'

def area_circle(radius_circle):
    """ This function returns the area of a circle """
    return f'Area of a circle - {round(pi * pow(radius_circle,2), 2)}'