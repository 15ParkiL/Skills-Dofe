def main(ans,operators): #ans is a list of numbers. [1,4,6,7,8] of any length, operators is a list of operators ['+','-','*']
    total = 0 # Starts the running answer
    for i in range(0,(len(operators))): # For amount of operators
        if i == 0: # If it is the first operator:
            if operators[i] == '+':
                total = (ans[i]) + (ans[i+1])
            elif operators[i] == '-':
                total = (ans[i]-ans[i+1])
            elif operators[i] == '*':
                total = (ans[i]*ans[i+1])
            elif operators[i] == '/':
                total = (ans[i]/ans[i+1])
            else:
                pass
        else: # If it isnt the first operator:
            if operators[i] == '+':
                total = total + ans[i]
            elif operators[i] == '-':
                total = total - ans[i]
            elif operators[i] == '*':
                total = total * ans[i]
            elif operators[i] == '/':
                total = total / ans[i]
            else:
                pass
    return(total) # Returns the output
