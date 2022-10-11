# Create a list that contains elements of integer type, then
# use the loop to change the type of these elements to a floating
# type.
# (Hint: use the built-in float () function).

natural_number = int(input('Enter a random natural positive number, please: '))

integer_list = [x*x for x in range(2, natural_number,2)] # create a list with elements of integer type
float_list = [float(i) for i in integer_list] # Change the type elements to floating type

print(float_list)