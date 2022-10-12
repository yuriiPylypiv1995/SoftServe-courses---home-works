# Create a function which answers the question "Are you playing banjo?".
# If your name starts with the letter "R" or lower case "r", you are playing banjo!
name = input("Are you playing banjo? Enter your name: ")

def are_you_playing_banjo(name):
    '''Returns string which answers the question "Are you playing banjo?" '''
    if name[0] == 'R' or name[0] == 'r':
        return f"{name} plays banjo"
    else:
        return f"{name} does not play banjo"

print(are_you_playing_banjo(name))