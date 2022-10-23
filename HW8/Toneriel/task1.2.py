import task1 

math_figures = input('Choose one of following math figures for calculate the area - rectangle, triangle or circle: ')

if math_figures == 'rectangle':
    length_rectangle = int(input('Enter the length of a rectangle: '))
    breadth_rectangle = int(input('Enter the breadth of a rectangle: '))
    print(task1.area_rectangle(length_rectangle, breadth_rectangle))
elif math_figures == 'triangle':
    base_triangle = int(input('Enter the base of a triangle: '))
    height_triangle = int(input('Enter a height of a triangle: '))
    print(task1.area_triangle(base_triangle, height_triangle))
elif math_figures == 'circle':
    radius_circle = int(input('Enter the radius of a circle: '))
    print(task1.area_circle(radius_circle))
else:
    print('Unfortunately, you have not selected any available mathematical figures. Have a nice day. Bye!')
    


