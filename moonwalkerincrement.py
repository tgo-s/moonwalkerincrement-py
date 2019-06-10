usrInput = input("Entre com o número inicial: ")

incrementer = 10
decrement = 1

def seeder(seed):
    decrementMultiplier = 1
    incrementerMultiplier = 1

    outputValue = seed + (incrementer * incrementerMultiplier) - (decrement * decrementMultiplier)

    if outputValue % 100 == 0:
        decrementMultiplier = 2
        incrementerMultiplier = 2
        pass
    else:
        if seed % 100 >= 90:
            decrementMultiplier = 2
        pass
    
        if seed % 10 == 0:
            incrementerMultiplier = 2
            pass
        pass
    
    outputValue = seed + (incrementer * incrementerMultiplier) - (decrement * decrementMultiplier)

    return outputValue
    pass

seed = int(usrInput)

for val in list(range(0,30)):
    seed = seeder(seed)
    print(f'[{val+1}][{seed:08}]')
    pass





