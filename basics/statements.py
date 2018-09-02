# if, elif, else

x = False

if x:
    print 'x was True'
else:
    print 'x was False'

loc = 'Bank'

if loc == 'Shop':
    print 'Welcome to the Shop'
elif loc == 'Bank':
    print 'Welcome to the Bank'
else:
    print 'Unknown'

# For Loops

l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in l:
    print num

print 'Even numbers'
for num in l:
    if num % 2 == 0:
        print num

print 'Dictionary iterator'
d = {'k1': 1, 'k2': 2, 'k3': 3}
for k, v in d.iteritems():
    print '{k}:{v}'.format(k=k, v=v)
