# Write a script that will calculate the factorial of the entered number
# without using recursion.

natural_number = int(input('Enter a random natural positive number, please: '))
factorial_number = 1

if natural_number < 0:
    print("Error! Enter a positive number. Next time. ")
elif 0 == natural_number < 1:
    print(f"Factorial of a number {natural_number} equal 1 ")
elif natural_number > 1:
    for i in range(2, natural_number + 1):
        factorial_number *= i
    print(f"Factorial of a number {natural_number} equal {factorial_number}")
     