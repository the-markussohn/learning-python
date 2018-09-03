import math
import string

# Methods
l = [1, 2, 3, 4, 5]

l.append(6)
print 'After append: ', l

print 'Result of count(1): ', l.count(1)

l.extend(range(7, 11))
print 'After extend: ', l

l.insert(1, 1)
print 'After insert: ', l

l.pop()
print 'After pop: ', l

l.remove(3)
print 'After remove(3): ', l

l.reverse()
print 'After reverse: ', l

l.sort()
print 'After sort: ', l


# Functions
def sayHello():
    print 'hello'

sayHello()


def add(a, b):
    return a + b

print add(15, 2)

# Lambdas
rev = lambda string: string[::-1]
print rev('hello')


# Homework
def vol(rad):
    return 4.0 / 3.0 * math.pi * rad**3

print vol(2)


def ran_check(num, low, high):
    return num in range(low, high + 1)

print ran_check(3, 1, 10)

s = 'Hello Mr. Rogers, how are you this fine Tuesday?'


def up_low(string):
    print 'No. of Upper case characters: ', sum(
        1 for c in string if c.isupper())
    print 'No. of Lower case characters: ', sum(
        1 for c in string if c.islower())

up_low(s)


def unique_list(l):
    return list(set(l))

print unique_list([1, 1, 1, 1, 2, 2, 3, 3, 3, 3, 4, 5])


def multiply(numbers):
    return reduce(lambda x, y: x * y, numbers)

print multiply([1, 2, 3, -4])


def palindrome(string):
    return string == string[::-1]

print palindrome('helleh')


def ispangram(string, alphabet=string.ascii_lowercase):
    return set(string.lower()) >= set(alphabet)


print ispangram("The quick brown fox jumps over the lazy dog")
