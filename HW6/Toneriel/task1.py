# In the range from 1 to 10 determine even numbers that are divisible by 2,
# odd numbers, which are divisible by 3, numbers that are not divisible by 2 and 3.

#realization by list comprehension

#determineeven numbers that are divisible by 2
list_divisible_by_even_num = [x for x in range(1,11) if x%2 == 0]
print(list_divisible_by_even_num)

#determine odd numbers, which are divisible by 3
list_divisible_by_odd_num = [x for x in range(1,11) if x%3 == 0 and x%2 != 0]
print(list_divisible_by_odd_num)

#determine numbers that are not divisible by 2 and 3
list_divisible_by_3_and_2 = [x for x in range(1,11) if x%2 == 0 and x%3 == 0]
print(list_divisible_by_3_and_2)

#realization by loop statements

#determineeven numbers that are divisible by 2
list_divisible_by_2 = []

for x in range(1,11):
    if x%2 == 0:
        list_divisible_by_2.append(x)
    else:
        continue
    
print(list_divisible_by_2)

#determine odd numbers, which are divisible by 3
list_divisible_by_3 = []

for x in range(1,11):
    if x%3 == 0 and x%2 != 0:
        list_divisible_by_3.append(x)
    else:
        continue
    
print(list_divisible_by_3)

#determine numbers that are not divisible by 2 and 3
list2_divisible_by_2_and_3 = []

for x in range(1,11):
    if x%2 == 0 and x%3 == 0:
        list2_divisible_by_2_and_3.append(x)
    else:
        continue
    
print(list2_divisible_by_2_and_3)
    