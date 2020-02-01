
import sliceprocessor
import acc
import crossbrack_acc

def pairbrackets(f,s): # Pairs up the inputted brackets based on their order.
    brackets = {}
    for i in range(0,len(f)):
        brackets[f[i]] = s[i]
    return brackets

def bracketparcing(string): ##---------------------------- TO DO: INTERNAL BRACKETTING. ((37485+2734)-(273)) * 2 <--- THIS BREAKS IT.
    firstbrackets = []
    secondbrackets = []
    for i in range(0,(len(string))): 
        if string[i] == '(': # Finds first bracket
            firstbrackets.append(i) #  Saves it
        elif string[i] == ')':# Finds second bracket
            secondbrackets.append(i) # Saves it
    if len(firstbrackets) != len(secondbrackets): # If there arent enough bracket starts and ends, returns an error message.
        brackets = 'SYNTAX ERROR'
    else:
        brackets = pairbrackets(firstbrackets,secondbrackets) # Pairs up the brackets 
    #okay so at this point, we have a dictionary which gives the location of all the brackets. Now we just need to seperate those brackets, while still keeping the seperate operators.
            
    return(brackets,string)

            

def space_removal(strlist): # Removes all spaces from the input.
    templist = []
    len(strlist)
    for i in range(len(strlist)): # Finds spaces in string (list) and identifies the element id of them.
        if strlist[i] == ' ':
            templist.append(i)
    for i in reversed(templist):
        del strlist[i] # Deletes spaces from string based on element ID
    return(strlist)

def calculate(dict): # For all the brackets in the dictionary, run the acc.calculate on them.
    ans = []
    for i in dict:
        ans.append(acc.calculate(dict[i])) #Adds the result of each bracket to the list ans
    return(ans)

def parsingengine(string):
    string = list(string) #Converts the input to a list
    string = space_removal(string) #removes any spaces from the list
    ##----------------#before this next part, it program needs to automatically add brackets in the correct locations.
    s1,s2 = bracketparcing(string) #Finds brackets in string
    bracketstring,operators = sliceprocessor.mainpro(s1,s2) #Returns the bracketed sections in seperate dictionary values. [In]
    ans = calculate(bracketstring) # Calculates answers of each bracket
    answer = crossbrack_acc.main(ans,operators) # Calculates answers of brackets operated on each bracket.
    return(answer)