#! python3
# Usage: py mcb.pyw save <keyword> - Saves clipboard to keyword.
#        py mcb.pyw <keyword> - Loads keyword to clipboard.
#        py mcb.pyw list - Loads all keywords to clipboard.
#        py mcb.pyw delete <keyword> - Deletes keyword from shelf
#        py mcb.pyw deleteAll - Deletes all keywords from the shelf

import shelve, pyperclip, sys

mcbShelf = shelve.open('mcb')

# save content
if len(sys.argv) == 3:
    if sys.argv[1].lower() == 'save':
        mcbShelf[sys.argv[2]] = pyperclip.paste()
    elif sys.argv[1].lower() == 'delete':
        del mcbShelf[sys.argv[2]]
elif len(sys.argv) == 2:
    # list keywords and load
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
    elif sys.argv[1].lower() == 'deleteall':
        for key in mcbShelf.keys():
            del mcbShelf[key]
    elif sys.argv[1] in mcbShelf:
        pyperclip.copy(mcbShelf[sys.argv[1]])

mcbShelf.close()