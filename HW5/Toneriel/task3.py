# Print Fibonacci numbers up to the entered number n,
# using cycles.
# (Sequence of Fibonacci numbers 0, 1, 1, 2, 3, 5, 8, 13, etc.)

number_for_fibonacci = int(input('Enter a random natural positive number, please: '))

fibonacci_list = [0,1]
previous_num =0
fib_number = 1
    
for i in range(2, number_for_fibonacci + 1):
    previous_num, fib_number = fib_number, previous_num + fib_number
    fibonacci_list.append(fib_number)

print(fibonacci_list)