#! python3

# append an astrix to the start of each line of text in clipboard

from pyperclip import copy, paste

text = paste()

lines = text.split('\n')
for i in range(len(lines)):
    lines[i] = '* ' + lines[i]

text = '\n'.join(lines)
copy(text)
print(paste())

