# when something becomes iterable:
# 	can use for loops,
#   feed it to set
#   feed it to sorted, min, max, heap, queue, sum
#   many tools consume iterators
# 	it will work with the rest of the functions in the python toolkit
# only issue, the function argument has to be a function of no arguments
# to turn function of many arguments to a function of fewer arguments use partial


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



# # looping backwards
# In C
for i in xrange(len(text)-1, -1, -1):
    print text[i]


# In Python
for word in reversed(text):
    print word


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
