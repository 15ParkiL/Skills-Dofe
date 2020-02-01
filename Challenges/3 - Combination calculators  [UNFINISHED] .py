def john(x):
  numlist = []
  for i in range(1,(x)):
    numlist.append(i)

  total = x
  if x == 0:
    print('1')
  else:
    for i in numlist:
      x = x * i
    print(x)
    return(x)
  

alpha = john(9)
beta = john(5)
alpha = int(alpha)
beta = int(beta)
print(alpha/beta)
