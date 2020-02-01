
def main():
  x = int(input('Initial number: '))
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
  

while 0 == 0:
  main()
