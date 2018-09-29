# 	Replace traditional index manipulation with Python's core looping idioms
# when you use index searching, unless exotic circumstance, should not be doing

# 	Learn advanced techniques with for-else clauses and the two argument form of iter()

# Goal: Improve your craftmanship and aim for clean fast, idimatic Python code

# looping over a range of numbers
for i in [0, 1, 2, 3, 4, 5]:
	print i**2
# python's for is not like other language "for", probably should be named foreach
# it loops over collections, using the iterator protocol

# a better way
for i in range(6):
	print i**2
# they do the same thing in exactly the same way
# range produces the same list and the for loops over the list

# if range(1000000), 32mb memorie

# better way
for i in xrange(6):
	print i**2
# produces an iterator over the range, giving the values one at a timec

# python3
# xrange was replaced with range










# looping over a collection/list
colors = ['red', 'green', 'blue', 'yellow']

# C
for i in range(len(colors)):
	print colors[i]

# in python it's faster
for color in colors:
	print color


# looping backwards
# C
for i in range(len(colors)-1, -1, -1):
	print colors[i]

# in python
for color in reversed(colors):
	print color

# looping over a collection and indicies
colors = ['red', 'green', 'blue', 'yellow']

# C
for i in range(len(colors)):
	print i, '-->', colors[i]

# python
for i, color in enumerate(colors):
	print i, '-->', colors[i]
# if manipulating indicies directly, it's probably wrong

# even better
for i, color in enumerate(colors):
	print i, '-->', color

# looping over two collections
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
	print names[i], '-->', colors[i]

# in python
for name, color in zip(names, colors):
	print name, '-->', color
# pretty slow, it generates a third tuples list, more memory than orig 2 lists combined, not fitting in L1 cache

# code should be running in L1 cache
# on cache miss a simple move goes from 1 clockcycle to 400-600 clock cycles, losing 2 oreders of magnitude
for name, color in izip(names, colors):
	print name, '-->', color
# iterators were done by Guido

# looping in sorted order
for color in sorted(colors):
	print color

# looping over reversed sorted list
for color in sorted(colors, reverse=True):
	print color


# Custom sort order
# the classic way, by making a custom comparison function
colors = ['red', 'green', 'blue', 'yellow']

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












# call function untill a sentinel value
# traditional way to do a repeated call over a function that has a sentinel value
#
# read block of strings, eventually run out of data, f.read returns a sentinel value, so when sentinel value is encountered we can break out of the loop
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
# 	can use for loops,
#   feed it to set
#   feed it to sorted, min, max, heap, queue, sum
#   many tools consume iterators
# 	it will work with the rest of the functions in the python toolkit
# only issue, the function argument has to be a function of no arguments
# to turn function of many arguments to a function of fewer arguments use partial
blocks = []
for block in iter(partial(f.read, 32), ''):
	blocks.append(block)










# Distinguishing multiple exit points in loops
# Donald Knuth came up with some structured equivalent
# need flag variable to say if something is found or not found
# the code could be returned/exited earlier when value is found, however this type of code is usually a portion of a bigger functionality thus can't be exited early
def find(seq, target):
	found = False
	for i, value in enumerate(seq):
		if value -- target:
			found = True
			break
	if not found:
		return -1
	return i

# a better way, the else clause
# basically, the for loop says:
# if loop not finished, keep doing the body
# if loop not finished, keep doing the body
# if body finished and no break was encountered - else
# so se can have an else clause, it's associated with if
# else should be called nobreak
# if it sould have that name, everybody would use it properly
def find(seq, target):
	for i, value in enumerate(seq):
		if value == target:
			break
	else:
		return -1
	return i
# in the future,
# emphasis on why it should be called no break
# two ways to exit the loop:
# 	finish it normally
# 	break out
# search your house for the keys, two outcomes
# 	find the keys
# 	searched all the rooms and didn't find
# if finished the loop and didn't encounter a break, do else
# should be called no break and everybody would know what it does
# just like if lambda would be called makefunction
# nobody would ask what lambda does anymore










# Dictionary skills
# fundamental tool expressing relationships, linking, counting and grouping

# looping over the keys
d = ['matthew': 'blue', 'rachel': 'green', 'raymond':'red']

for k in d:
	print k
# Guido asked what should the for loop do with the dictionary
# half of the people were saying looping over the keys
# the other half was about looping over the keys and values
# Raymond grepped in a lot of existing code to find out the most common use case
# what was consistent with the list, the dictionary has the keys in a list

# another way
for k in d.keys():
	if k.startswith('r'):
		del[k]
# this should be done when the dictionary is mutated
# one should never mutate something while iterating over it, in any language
# example example example
# https://www.bennadel.com/blog/2992-mutating-an-array-during-foreach-iteration-in-javascript.htm
# https://stackoverflow.com/questions/10812272/modifying-a-list-while-iterating-over-it-why-not
# The reason to why you should never modify a list while iterating over it is for example, you're iterating over a list of 20 digits, and if you hit an even number you pop it off the list and carry on till you have a list of just odd numbers.

# Now, say this is your sample data [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], and you start iterating over it. First iteration, and the number is 1 so you continue, the following number is 2 so you pop it off, and rinse and repeat. You now feel the application worked correctly as the resultant list is [1, 3, 5, 7, 9, 11, 13, 15, 17, 19].

# Now let's say your sample data is [1, 2, 4, 5, 7, 8, 10, 11, 12, 13, 15, 15, 17, 18, 20] and you run the same piece of code as before and mutate the original list while iterating through it. Your resultant list is [1, 4, 5, 7, 10, 11, 13, 15, 15, 17, 20] which is clearly incorrect as there are still even numbers contained in the list.

# If you are planning on mutating the list while iterating through it like so

# for elem in lst:
#     # mutate list in place
# You should rather change it to

# for elem in lst[:]:
#     # mutate list in place
# The [:] syntax creates a new list that is an exact copy of the original list, so that you can happily mutate the original list without affecting what you're processing as you won't have any unintended side-effects from mutating the list you're iterating through.

# If your list is rather sizable, instead of creating a new list and stepping through it look at using generator expressions or write your own generator for your list if you feel the need so that you do not waste memory and CPU cycles.

# d.keys() makes a copy of the list and stores it in a list
# the dictionary can be mutated

# even better
d = {k : d[k] for k in d if not k.startswith('r')}

# looping over dictionary keys and values
for k in d:
	print k, '-->', d[k]
# not fast because it has to rehash every key and do a lookup on it

# a better way
for k, v in d.items():
	print k, '-->', v
# tuple unpacking, no lookups involved

# a better way, because items() produces a big huge list, we have iteritems()
for k, v in d.iteritems():
	print k, '-->', v
# iteritems() returns an iterator so it can be fed to all the things
# Barry Warsaw





# Counting with dictionaries
colors = ['red', 'green', 'red', 'blue', 'green', 'red']
d = {}
for color in colors:
	if color not in d:
		d[color] = 0
	d[color] += 1
{'blue': 1, 'green': 2, 'red': 3}
# look up the dictionary, see if the value is there
# and if it's not, add it
# a better way
d = {}
for color in colors:
	d[color] = d.get(color, 0) + 1
# get the color, if the color is missing, add 1 to the 0
# a better way
d = defaultdict(int)
for color in colors:
	d[color] += 1
# factory functions
# int can be called with no argument, producing the value 0
# return a defaultdict which sometimes behaves different than dict




# grouping with dictionaries
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

d = {}
for name in names:
	key = len(name)
	if key not in d:
		d[key] = []
	d[key].append(name)
# start with an empty dictionary
# the key is the value one wishes to group by
# e.g. raymond is of length 7, along with all the names
# to group by anything else, just change the key line
# e.g. by the first letter, thumber if e in the name
# a better way
d = {}
for name in names:
	key = len(name)
	d.setdefault(key, []).append(name)
#
# we need to return the list so we can append to it
# but also need to be inserted in
# setdefault is just like get but has the side effect of
# inserting the missing key
# e.g. this goes into the dictionary see if the key is there
# if it's not, takes the default value and inserts it
# and returns it so you can group with it
# a better way
d = defaultdict(list)
for name in names:
	key = len(name)
	d[key].append(name)
# wherever you see #326
# do this instead
# looks better, is faster










# IS a dictionary popitem() atomic?
d = {'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}

while d:
	key, value = d.popitem()
	print key, '-->', value
# something about putting docstrings everywhere in the project
# and as a side effect, you learn what every module does
# removes an arbitrary item, it is atomic, you don't have to put locks on it
# can be used between threads






# Linking dictionaries



























# Construct a dictionary from pairs
names = ['raymnd', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']





##
