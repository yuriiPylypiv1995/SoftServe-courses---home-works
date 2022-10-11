natural_number = int(input('Enter a four-digit natural number, please: '))

list_natural_number = [int(x) for x in str(natural_number)]

# multiply natural number
multiply_natural_number = 1

for i in range(0, len(list_natural_number)):
    multiply_natural_number = multiply_natural_number * list_natural_number[i]

print(f'Multiplied natural number: {multiply_natural_number}')

# reverse natural number
reverse_natural_number = 0

while natural_number > 0:
    modulus_num = natural_number % 10
    reverse_natural_number = reverse_natural_number * 10 + modulus_num
    natural_number //= 10

print(f'Reversed natural number: {reverse_natural_number}')

# sort number

list_natural_number.sort()

convert_from_int_to_str = [str(i) for i in list_natural_number]
new_string = "".join(convert_from_int_to_str)

sort_natural_number = int(new_string)

print(f'Sorted natural number: {sort_natural_number}')


