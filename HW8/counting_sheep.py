# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).

array1 = [True,  True,  True,  False,
          True,  True,  True,  True ,
          True,  False, True,  False,
          True,  False, False, True ,
          True,  True,  True,  True ,
          False, False, True,  True, None ]
          
def count_sheeps(sheep):
    '''Returns the number of True in the array.'''
    return sheep.count(True)

print(count_sheeps(array1))