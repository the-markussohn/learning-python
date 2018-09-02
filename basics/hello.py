S = 'Hello'
print S

# Dictionary
D = {}
D['foo'] = 'bar'
print 'D: {s}'.format(s=D.keys())

# Tuples
t = ('one', 2)
print 'One shows up: {s}'.format(s=t.count('one'))

# Files
# Reading
inputFile = open('test.txt')
print inputFile.read()
inputFile.close()

# Writing
outputFile = open('test_w.txt', 'w+')
outputFile.write('This is a new line in test file!')
outputFile.seek(0)
print outputFile.read()
outputFile.close()

# Sets
x = set()
x.add('set')
print x

l = [1, 1, 2, 2, 3, 4, 5, 6, 1, 1]
sFromL = set(l)
print sFromL

# Test
print 'Test'
s = 'hello'

print s[1]
print s[::-1]
print s[-1]
print s[-1:]

l1 = [0]*3
l2 = [0, 0, 0]
print l1
print l2
l = [1, 2, [3, 4, 'hello']]
l[2][2] = 'goodbye'
print l
l = [5, 3, 4, 6, 1]
print sorted(l)
d = {'simple_key': 'hello'}
# Grab 'hello'
print d['simple_key']
d = {'k1': {'k2': 'hello'}}
# Grab 'hello'
print d['k1']['k2']
# Getting a little tricker
d = {'k1': [{'nest_key': ['this is deep', ['hello']]}]}

# Grab hello
print d['k1'][0]['nest_key'][1][0]

# This will be hard and annoying!
d = {'k1': [1, 2, {'k2': ['this is tricky', {'tough': [1, 2, ['hello']]}]}]}
print d['k1'][2]['k2'][1]['tough'][2][0]

l = [1, 2, 2, 33, 4, 4, 11, 22, 3, 3, 2]
print set(l)

print 3.0 == 3