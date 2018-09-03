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

# While loops
x = 0
while x < 10:
    print 'x is currently: ', x
    x += 1
else:
    print 'Done!'

# range()
start = 0
stop = 20
x = range(start, stop, 2)
print x

# Comprehensions
l = []

for letter in 'word':
    l.append(letter)

print l

l = [letter for letter in 'word']
print l

# Test
print "Use for, split(), and if to create a Statement that will print out words that start with 's':"
st = 'Print only the words that start with s in this sentence'
for word in st.split(' '):
    if word.lower()[0] == 's':
        print word

print "Use range() to print all the even numbers from 0 to 10."
print range(0, 11, 2)

print "Use List comprehension to create a list of all numbers between 1 and 50 that are divisible by 3."
l = [num for num in range(1, 50) if num % 3 == 0]
print l

print "Go through the string below and if the length of a word is even print 'even!'"
st = 'Print every word in this sentence that has an even number of letters'
for word in st.split():
    if len(word) % 2 == 0:
        print word, ' is even!'

print 'FizzBuzz program'
for num in range(1, 101):
    if num % 5 == 0:
        if num % 3 == 0:
            print 'FizzBuzz'
        else:
            print 'Buzz'
    elif num % 3 == 0:
        print 'Fizz'
    else:
        print num

print "Use List Comprehension to create a list of the first letters of every word in the string below:"
st = 'Create a list of the first letters of every word in this string'
l = [word[0] for word in st.split()]
print l
