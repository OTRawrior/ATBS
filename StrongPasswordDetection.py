#! python3
"""Write a function that uses regular expressions to make sure the password
string it is passed is strong. A strong password is defined as one that is at
least eight characters long, contains both uppercase and lowercase characters,
and has at least one digit. You may need to test the string against multiple
regex patterns to validate its strength."""

import re

password = input('Please enter your password: ')

strongLength = re.compile(r'.{8}')

strongUpper = re.compile(r'[A-Z]')

strongLower = re.compile(r'[a-z]')

strongDigits = re.compile(r'\d')

if strongLength.search(password) != None:
    if strongUpper.search(password) != None and strongLower.search(password) != None:
        if strongDigits.search(password) != None:
            print(password + ' is a strong password.')
        else:
            print('Passwords must contain at least one digit.')
    else:
        print('Passwords must contain both upper and lower case characters.')
else:
    print('Passwords must be at least 8 characters.')