def main(gate):
    a = input('')
    b = input('')
    if gate == "OR":
        if a == '1':
            return('1')
        else:
            if b == '1':
                return('1')
            else:
                return('0')
    elif gate == "AND":
        if a == "0":
            return('0')
        elif b == "0":
            return('0')
        else:
            return('1')
    elif gate == "XOR":
        if a == '1':
            return('0')
        elif b == '1':
            return('0')
        else:
            return('1')
    elif gate == "NAND":
        if a == '1':
            if b == '1':
                return('0')
            else:
                return('1')
        else:
            return('1')
    elif gate == "NOR":
        if a == "1":
            return('0')
        else:
            return('1')
        if b == "1":
            return('0')
        else:
            return('1')
    else:
        return('Not a valid gate, Try all capitals')
        
        
        
    
while 0 == 0:
    print(main(input('Logic Gate (OR/AND/XOR/NAND/NOR): ')))
