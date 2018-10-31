# # looping backwards
# In C
for i in xrange(len(text)-1, -1, -1):
    print text[i]


# In Python
for word in reversed(text):
    print word


# looping in sorted order
colors = ['red', 'green', 'blue', 'yellow']

for color in sorted(colors):
	print color

# looping over reversed sorted list
for color in sorted(colors, reverse=True):
	print color


# Custom sort order
# the classic way, by making a custom comparison function

def compare_length(c1, c2):
	if len(c1) < len(c2): return -1
	if len(c1) > len(c2): return 1
	return 0

print sorted(colors, cmp=compare_length)
# on 1 000 000, Nlog(N) comparations - 20 000 000 comparations

# a better way
print sorted(colors, key=len)
# called once per key, on 1 000 000, called 1 000 000 times
# from sql, everything is ordered but not by comparison function
# in python3 - no more comparison functions


for count in xrange(1000):
    with open('sample.txt', 'w') as f:
        for i in xrange(len(text)-1, -1, -1):
            f.write(text[i])
# 72005 function calls in 0.214 seconds


for count in xrange(1000):
    with open('sample.txt', 'w') as f:
        for word in reversed(text):
            f.write(word)
# 70004 function calls in 0.206 second



# call function untill a sentinel value
# traditional way to do a repeated call over a function that has a sentinel value
#
# read block of strings, eventually run out of data, f.read returns a sentinel value, so when 
# sentinel value is encountered we can break out of the loop
# build blocks of strings, output is big list of strings
# should connect together strings with join
# should not connect together strings with +
blocks = []
while True:
    block == f.read(32)
    if block == '':
        break
    blocks.append(block)

# this code does the same thing

# new
# the iter function can take 2 arguments
# 1: the function that you call over and over again
# 2: sentinel value
# the ITER function
# will call read over and over again, looping over a block of 32 bits
# when sentinel value is encountered, break out of the loop
#
# when something becomes iterable:
#   can use for loops,
#   feed it to set
#   feed it to sorted, min, max, heap, queue, sum
#   many tools consume iterators
#   it will work with the rest of the functions in the python toolkit
# only issue, the function argument has to be a function of no arguments
# to turn function of many arguments to a function of fewer arguments use partial
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)