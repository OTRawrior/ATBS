spam = ['a', 'b', 'c', 'd']

def listAnd(list):
    result = ''
    for x in range(len(list)-1):
        result += list[x]
        result += ', '
    result += 'and '
    result += list[len(list)-1]
    return result
        
print(listAnd(spam))