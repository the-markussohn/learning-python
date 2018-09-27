from sys import argv

#Some dumb ones to get the feeling
def print_some(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)

def print_one(arg1):
    print "arg1: ", arg1

print_some("the", "markussohn")
print_one("the-markussohn")

#Some files

script, input_file = argv

def print_all(f):
    print f.read()

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "Printing whole file:\n"

print_all(current_file)

rewind(current_file)

print "Printing 2 lines"

current_line = 1

print_a_line(current_line, current_file)
print_a_line(current_line + 1, current_file)

#Functions with return

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

print "Some math:"
age = add(32, 3)
height = subtract(200, 12)

print "Age: %d, Height: %d" % (age, height)