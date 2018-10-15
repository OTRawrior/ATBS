def collatz(number):
    if number % 2 == 0:
        return(number // 2)
    else:
        return(3*number + 1)

while True:
    try:        
        global x 
        x = collatz(int(input("Pick a number: ")))
        break
    except:
        print("A number, please.")
        
while x != 1:
    print(x)
    x = collatz(x)
print(x)