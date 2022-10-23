# Write a program that calculates the area of ​a rectangle,
# triangle and circle
# (write three functions to calculate the area, and call them in the
# main program depending on the user's choice).

from math import pi 

def area_rectangle(length_rectangle, breadth_rectangle):
    """ This function returns the area of a rectangle """
    return f'Area of a rectangle - {length_rectangle * breadth_rectangle}'

def area_triangle(base_triangle, height_triangle):
    """ This function returns the area of a triangle """
    return f'Area of a triangle - {1/2 * base_triangle * height_triangle}'

def area_circle(radius_circle):
    """ This function returns the area of a circle """
    return f'Area of a circle - {round(pi * radius_circle**2, 2)}'

#main program
math_figures = input('Choose one of following math figures for calculate the area - rectangle, triangle or circle: ')

if math_figures == 'rectangle':
    length_rectangle = int(input('Enter the length of a rectangle: '))
    breadth_rectangle = int(input('Enter the breadth of a rectangle: '))
    print(area_rectangle(length_rectangle, breadth_rectangle))
elif math_figures == 'triangle':
    base_triangle = int(input('Enter the base of a triangle: '))
    height_triangle = int(input('Enter a height of a triangle: '))
    print(area_triangle(base_triangle, height_triangle))
elif math_figures == 'circle':
    radius_circle = int(input('Enter the radius of a circle: '))
    print(area_circle(radius_circle))
else:
    print('Unfortunately, you have not selected any available mathematical figures. Have a nice day. Bye!')
    