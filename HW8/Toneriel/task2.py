# Write a Python program to check the validity of a password (input from users).

# Validation :
# At least 1 letter between [a-z] and 1 letter between [A-Z].
# At least 1 number between [0-9].
# At least 1 character from [$#@].
# Minimum length 6 characters.
# Maximum length 16 characters.

import re 

user_password = input('Password must contain between 6 and 16 characters, including at least 1 lowercase letter, 1 uppercase letter, 1 number, and at least 1 -$,#,@ character: ')

def validate_password(user_password):
    """Returns True only if password is strong enough."""
    pattern=r'[A-Z|a-z|0-9|.$#@]{6,16}'
    match_password = re.fullmatch(pattern, user_password)
    if bool(match_password) == True:
        return 'Thank you. Your password is valid.'
    else:
        return 'Your password is incorrect. Try again.'
    
print(validate_password(user_password))