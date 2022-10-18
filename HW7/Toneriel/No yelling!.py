# Write a function taking in a string like WOW this is REALLY 
# amazing and returning Wow this is really amazing. 
# String should be capitalized and properly spaced. Using re and string is not allowed.

def filter_words(st):
    """ This function gets the capitalized text without extra spaces. """
    return ' '.join(st.capitalize().split())

print(filter_words('HELLO    wOrld! '))