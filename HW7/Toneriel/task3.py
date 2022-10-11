# Write a function that calculates the number of characters
# included in a given string

# • input: "hello"
# • output: {"h":1, "e":1,"l":2,"o":1}

def number_characters(characters):
    """ This function calculates the number of characters included in a given string. Returns a dictionary. """   
    list_characters = []
    list_characters.extend(characters.replace(" ", ""))
    dict_characters = {}.fromkeys(list_characters)
    for k,v in dict_characters.items():
        dict_characters[k] = list_characters.count(k)
        
    return dict_characters

print(number_characters("hello world"))
    