people = 20
cats = 30

if people < cats:
    print "Too many cats"

if people > cats:
    print "Enough humans"

cars = 20

if people < cars:
    print "Too many cars"
elif people > cars:
    print "Not enough cars"
else:
    print "Yay"


the_count = [1, 2, 3, 4, 5]

for number in the_count:
    print number

elements = []

for i in range(0, 6):
    elements.append(i)

for i in elements:
    print i