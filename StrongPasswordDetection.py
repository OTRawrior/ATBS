#! python3
'''Write a function that uses regular expressions to make sure the password 
string it is passed is strong. A strong password is defined as one that is at 
least eight characters long, contains both uppercase and lowercase characters, 
and has at least one digit. You may need to test the string against multiple 
regex patterns to validate its strength.'''


import re

#password = input('Please enter your password: ')

strongLength = re.compile(r'''(
        

)''', re.VERBOSE)

strongCases = re.compile(r'''(
        

)''', re.VERBOSE)

strongDigits = re.compile(r'''(
        

)''', re.VERBOSE)