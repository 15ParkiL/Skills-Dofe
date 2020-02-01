print('Format must be in  HH-MM')
first = str(input('First timestamp:'))
second = str(input('Second timestamp:'))

first = first.split("-")
second = second.split("-")
firsthour = int(first[0]) * 60
secondhour = int(second[0]) * 60
firsttotal = firsthour + int(first[1])
secondtotal = secondhour + int(second[1])
timetaken = secondtotal - firsttotal
timetaken = timetaken/60

print(1/timetaken)
