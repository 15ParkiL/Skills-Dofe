firsttotal = 0
secondtotal = 0

first = [ord(c) for c in input()]
second = [ord(c) for c in input()]

for i in range(0, len(first)):
  firsttotal = firsttotal + first[i]
for i in range(0, len(second)):
  secondtotal = secondtotal + second[i]

print(firsttotal,'-',secondtotal,'=',(firsttotal - secondtotal))
