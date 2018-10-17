inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def displayInventory(inv):
    print('Inven')
    itemTotal = 0
    for k, v in inv.items():
        print(str(v) + ' ' + k)
        itemTotal += v
    print('Total items: ' + str(itemTotal))
    
def addToInventory(inventory, addedItems):
    for loot in addedItems:
        inventory.setdefault(loot, 0)
        inventory[loot] += 1
    return(inventory)
    

inv = addToInventory(inv, dragonLoot)


displayInventory(inv)
