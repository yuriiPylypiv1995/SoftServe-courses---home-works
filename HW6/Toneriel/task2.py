# Write a script that checks the login that the user enters. 
# If the login is "First", then greet the users. If the login is
# different, send an error message. (need to use loop while)

true_user_login =  input('Enter user login: ')

while true_user_login != 'First':
    print('Error! Enter the correct user login or enter: "Logout"') 
    true_user_login = input('Enter user login: ')
    if true_user_login == 'Logout':
        break
    continue
else: 
    print('Greetings to you')
    