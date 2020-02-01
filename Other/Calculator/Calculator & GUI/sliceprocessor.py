def mainpro(brackets,l):
    #Init variables
    x = {}
    y = 0
    z = {}
    
    for i in brackets:
        first = ((int(i))+1)
        second = int(brackets[i])
        x[y] = (l[first:second])
        try: ##FINDS the between-brackets operator
            z[y] = l[second+1] #Adds operator to dict z
        except: ## if at the end of the list, doesnt crash.
            break
        y += 1
    return(x,z)