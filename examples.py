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




# Construct a dictionary from pairs
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(izip(names, colors))
{'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}
# the dictionary constructor accepts a list of pairs or any iterable of pairs
# easiest way to construct the list of pairs is to izip them together
# parts of python fit beatifully together
# how do you take two lists and construct them seamlesly into a dictionary:
# 4 words of python
# it doesn't make a tuple after each iteration
# iterates over the same tuple over and over again, without making calls to the
# allocator






# Linking dictionaries
defaults = {'color':'red', 'user':'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('=c', '--color')
namespace = parser.parse_args([])
command_line_args = {k:v for k, v in 
					 vars(namespace).items() if v}
# one dictionary with some default value for some parameters
# we call argparse and check for some command line arguments which are optional
# we also want to use the os.environ dictionary, to check for the values which are 
# os specific
# the default way to do it
d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)
# take the dictionary from the defaults
# than do an update on the defaults from the environment variables
# that way you got some standard defaults
# than the environment variables which take precedence over the standard defaults
# than the user specified variables

d = ChainMap(command_line_args, os.environ, defaults)
# python3
# it links them all together






# Improving clarity
# positional arguments and indices are nice
# keywords and names are better
# the first way is convenient for the computer
# the second corresponds to how humans think



# clarify function calls with keyword arguments
ts('@obama', False, 20, True)
# check everywhere one makes an obscure call like this
twitter_search('@obama', retweets=False, numtweets=20, popular=True)
# replace with keyword arguments



# clarify multiple return values with named tuples
# in the past
doctest.testmod()
# returned
(0, 4)
# now it returns
TestResults(failed=0, attempted=4)
# to define the named tuple
TestResults = namedtuple('TestResults', ['failed', 'attempted'])
# all your output messages and error messages will be more readable
# the person that benefits most of this is you





# unpacking sequences
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

# every other programming language
fname = p[0]
lname = p[1]
age = p[2]
email = p[3]

# a better way and faster
fname, lname, age, email = p



# updating multiple state variables
# simultainous state updates
def fibonacci(n):
	x = 0
	y = 1
	for i in range(n):
		print x
		t = y
		y = x + y
		x = t
# take a temporary variable and store the old y
# update the y with it's new alue
# set the new x

# using the tuple packing and unpacking
# y and x + y use the old values of x and y
# x and y are state, should be updated all at once
# if the state is updated on multiple lines
# inbetween the lines, the state is mismatched
# y is the new y and x is the old x
# the ordering matters
# the lines can be mixed up, it's broken down in subatomic particles
# too low level
# the first says
# take y and store in t
# take x + y and store to y
# take t and store in x
# the second says
# update these variables acording to those equations

# a better way
def fibonacci(n):
	x, y = 0, 1
	for i in range(n):
		print x
		x, y = y, x+y
# a higher level way of thinking
# don't under-estimate the advantages of updating state variables at the same time
# it eliminates an entire class of errors due to out of order updates
# it allows higher level thinking and lessens the chunking of thoughts



# efficency
# don't cause data to move around unecesarily
# it takes only a little care to avoit O(n**2) behaviour instead of linear behavior

# concatenating strings
names = ['raymond', 'rachel', 'matthew', 'roger', 
	     'betty', 'melissa', 'judith', 'charlie']

s = names[0]
for name in names[1:]:
	s += ', ' + name
print s
# quadratic

# linear
print ', '.join(names)




# updating sequences 
names = ['raymond', 'rachel', 'matthew', 'roger',
	     'betty', 'melissa', 'judith', 'charlie']

# wherever you see you are probably doing it wrong or using an incorrect 
# data structure. Each of these operations are O(N) on lists
del names[0]
names.pop(0)
names.insert(0, 'mark')

names = deque(['raymond', 'rachel', 'matthew', 'roger',
	           'betty', 'melissa', 'judith', 'charlie'])

# O(1) on deque
del names[0]
names.popleft()
names.appendleft('mark')








# decorators and context managers
# Helps separate business logic from administrative logic
# Clean, beautiful tools for factoring code and improving code reuse
# good naming is esential
# Remember the spiderman rule: with great power comes great responsibility



# using decorators to factor-out administrative logic
def web_lookup(url, saved={}):
	if url in saved:
		return saved[url]
	page = urllib.urlopen(url).read()
	saved[url] = page
	return page
# business logic is opening an url and returning the web page
# administrative logic is caching it in a dictionary, that way if I lookup the same
# webpage, we will serve it from cache
# mixes admin logic with business logic and is not reusable

# simple fix
@cache
def web_lookup(url):
	return urllib.urlopen(url).read()
# @cache can be put in front of any pure function
# A pure function is a function where the return value is only determined by its
# input values, without observable side effects
# random.random is not a pure function

# the caching decorator
def cache(func):
	saved = {}
	@wraps(func)
	def newfunc(*args):
		if args in saved:
			return newfunc(*args)
		result = func(*args)
		saved[args] = result
		return result
	return newfunc





# factor out temporary contexts
old_context = getcontext().copy()
getcontext().prec = 50
print Decimal(355) / Decimal(113)
set_context(old_context)
# copy the context, change the decimal precision, do a calculation and 
# set the new context. Saving the old, restoring the new

# there is a better way, with local context
with localcontext(Context(prec=50)):
	print Decimal(355) / Decimal(113)
# the context manager makes a copy of the context, sets in in place,
# does the calculation and restore it
# pretty much where you have set up logic and tear down logic in your code, 
# you want a context manager to improve it



# How to open and close files
f = open('data.txt')
try:
	data = f.read()
finally:
	f.close()
# the try, the finally that closes the "reader"

# the new way
with open('data.txt') as f:
	data = f.read()
# it factored out the setup logic and tear down logic

 

# how to use locks
# make a lock
lock = threading.Lock()

lock.acquire()
try:
	print 'Critical section 1'
	print 'Critical section 2'
finally:
	lock.release()
# acquire the lock, do a try finally
# do you have to do a try finally?
# absolutely
# because in some situations you don't release the lock if 
# an error happens in the block
# What happens when you don't release a lock?
# Puppies die?!

# the new way
with lock:
	print 'Critical section 1'
	print 'Critical section 2'
# separated the administrative logic - getting the lock



# factoring out temporary contexts
try:
	os.remove('somefile.tmp')
except OSError:
	pass
# do os.remove for file and catch an OS error
# another way is to check if the file exists before removing it
# it is not the right way because it has a raise condition in it
# so this above is the correct way

# a better way
with ignored(OSError):
	os.remove('somefile.tmp')

# Context manager: ignored()
@contextmanager
def ignored(*exceptions):
	try:
		yield
	except exceptions:
		pass
# this gets rid of the idiom for Try Except Pass


# factor out temporary contexts
with open('help.txt', 'w') as f:
	oldstdout = sys.stdout
	sys.stdout = f
	try:
		help(pow)
	finally:
		sys.stdout = oldstdout
# help redirects to stdoutput, if you want to store the output in a file
# open a file, redirect stdoutput temporary assign it
# do a try finally on the help, capturing the output

# a better way
with open('help.txt', 'w') as f:
	with redirect_stdout(f):
		help(pow)

# context manager: redirect_stdout()
@contextmanager
def redirect_stdout(fileobj):
	oldstdout = sys.stdout
	sys.stdout = fileobj
	try:
		yield fileobj
	finally:
		sys.stdout = oldstdout

# concise expressive oneliners

# two confilcting rules:
# 1. Don't put too much on one line
# 2. Don't break atoms if thought into subatomic particles

# Raymond's rule
# one logical line of code equals to one sentence in English


# the sum of the squares of numbers up to 10
result = []
for i in range(10):
	s = i ** 2
	result.append(s)
print sum(result)

print sum([i**2 for i in xrange(10)])
# why is it better
# the first one tells you what to do, step by step
# the second one says what you want, is more declarative
# it says, read it from left to right 
# I want the sum of the squares of i, for i from 1 to 10
# it's a single unit of thought 
# the first one just tells you how to do it and not what it's doing

# a better way
print sum(i**2 for i in xrange(10))
# taking out the brackets
# generator expressions
# creates a generator expression of this, instead of filling up memory
































