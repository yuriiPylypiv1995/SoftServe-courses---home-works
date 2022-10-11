with open('ZenPython') as f:
    lines = f.read()

count_better = lines.count('better')
count_never = lines.count('never')
count_is = lines.count('is')

print(f'Count of word \'better\': {count_better}')
print(f'Count of word \'never\': {count_never}')
print(f'Count of word \'is\': {count_is}')

zen_python_in_uppercase = lines.upper()

print(zen_python_in_uppercase)

replace_character = lines.replace('i', '&')

print(replace_character)



