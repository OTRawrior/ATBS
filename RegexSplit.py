"""Write a function that takes a string and does the same thing as the strip() string method. If no other arguments
are passed other than the string to strip, then whitespace characters will be removed from the beginning and end of
the string. Otherwise, the characters specified in the second argument to the function will be removed from the
string. """

# ! python2

import re

string = '                  some   texty stuff                 '


def regex_split(text, junk = '\s*'):
    if junk == '\s*':
        junk1 = '^' + junk
        junk2 = junk + '$'
    else:
        junk1 = junk
        junk2 = junk
    regex1 = re.compile(junk1)
    regex2 = re.compile(junk2)
    text = regex1.sub('', text)
    text = regex2.sub('', text)
    return text

string = input('what string')
remove = input('remove what')

if remove == '':
    print(regex_split(string))
else:
    print(regex_split(string, remove))