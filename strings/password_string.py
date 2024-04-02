length = lower = upper = digit = False

password = input('Enter the password: ')

if len(password)>= 8:
    length = True
    
    for letter in password:
        if letter.islower():
            lower = True
        elif letter.isupper():
            upper = True
        elif letter.isdigit():
            digit = True


if length and lower and upper and digit:
    print('That is a valid password.')
else:
    print('That password is not valid.')
