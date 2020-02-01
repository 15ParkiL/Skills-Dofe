numbers = ['1','2','3','4','5','6','7','8','9','0','.','^'] # List of numbers and ^
reals = ['1','2','3','4','5','6','7','8','9','0','.'] # List of numbers and .



def contpower(list): #Checks if there are powers. If so, works them out.
    power = False # Assumes it isnt a power
    for i in range(len(list)): # Iterates through list
        num = False 
        for x in reals:
            if list[i] == x:
                num = True
        if num == False: 
            power = True
            defin = i # Identifies the location in the list of the power symbol
    if power == True: # if there is a ^
        FA = ''.join(list[0:defin]) # Finds the first number 
        FB = ''.join(list[(defin+1):len(list)]) # Finds the second number
        return(float(FA)**float(FB)) # Returns the calculated first number to the power of the second number.
    else:
        returnval = ''.join(list[0:len(list)]) # If there isnt a power, joins the list into a single number.
        return(returnval) # Returns the above.

def findparts(strlist): # Seperates a very simple formula into three parts, first number, second number and operator.
    operator = '' # Init operator variable
    for i in range(len(strlist)): # For all elements in the list
        num = False # Assume it isnt a number until proven otherwise
        for x in numbers: 
            if strlist[i] == x:
                num = True # If it is a number (or a power or decimal), sets number as true.
        if num == False: # If it isnt a number (or a power or decimal), saves that operator
            operator = strlist[i]
            defin = i # Sets defin to the number in the list where the operator is
    firstnum = strlist[0:defin] # Sets the first number to all the numbers and decimals before the operator
    secondnum = strlist[(defin+1):len(strlist)]  # Sets the second number to all the numbers and decimals after the operator
    firstnum = contpower(firstnum) #Checks if there are powers. If so, works them out, and returns answer.
    secondnum = contpower(secondnum) #Checks if there are powers. If so, works them out, and returns answer.
    firstnum = float(firstnum) # Ensures it is a float
    secondnum = float(secondnum) # Ensures it is a float
    return(operator,firstnum,secondnum) # Returns the operator and answers.


    

def calculate(strlist):
    op,first,second = findparts(strlist) # Works out the 3 parts, (first and second number and operator) of a formula.
    if op == '*': # If operator is * multiplies it
        return(first * second)
    elif op == '/': # If operator is / divides it
        return(first / second)
    elif op == '+': # If operator is + adds it
        return(first + second)
    elif op == '-': # If operator is - subtracts it
        return(first - second)
    else:
        return('No valid operator') # If no valid operator can be found returns an error.



