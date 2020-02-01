from random import randrange
print(randrange(10))
while 0 == 0:
  input('Ready?')
  for i in range(1,10):
    numone = (randrange(99))
    numtwo = (randrange(99))
    op = (randrange(1))
    if op == (1):
      ans = input('What is ',numone,' + ',numtwo)
      if ans == (numtwo+numone):
        print('Correct')
        points = points + 1
      else:
        print('Incorrect')

    else:
      if numone > numtwo:
        ans = input('What is ',numone,' - ',numtwo)
        if ans == (numone-numtwo):
          print('Correct')
          points = points + 1
        else:
          print('Incorrect')
      else:
        ans = input('What is ',numtwo,' 0 ',numone)
        if ans == (numtwo-numone):
          print('Correct')
          points = points + 1
        else:
          print('Incorrect')
