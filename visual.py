# Idiomatic Pyton 

# Jeff Knupp said in "Writing Idiomatic Python"
# We may document our code extensively, write exhaustive unit tests,
# and hold code reviews three times a day, but the fact remains: when 
# someone else needs to make changes, the code is king
















































# looping over a range of numbers
for i in [0, 1, 2, 3, 4, 5]:
	print i**2















































# looping over a range of numbers
for i in [0, 1, 2, 3, 4, 5]:
	print i**2


# a better way
for i in range(6):
	print i**2


















































# looping over a range of numbers
for i in [0, 1, 2, 3, 4, 5]:
	print i**2


# a better way
for i in range(6):
	print i**2
# they do the same thing in exactly the same way



# better way
for i in xrange(6):
	print i**2

















































# looping over a range of numbers
for i in [0, 1, 2, 3, 4, 5]:
	print i**2


# a better way
for i in range(6):
	print i**2


# better way
for i in xrange(6):
	print i**2


# python3
# xrange was replaced with range

# /usr/bin/python2.7 -m timeit '"-".join([str(n) for n in xrange(1000000)])'
# 10 loops, best of 3: 263 msec per loop
# /usr/bin/python2.7 -m timeit '"-".join([str(n) for n in range(1000000)])'
# 10 loops, best of 3: 272 msec per loop

# /usr/bin/python2.7 -m timeit '"-".join([str(n) for n in range(10000000)])'
# 10 loops, best of 3: 2.58 sec per loop
# /usr/bin/python2.7 -m timeit '"-".join([str(n) for n in xrange(10000000)])'
# 10 loops, best of 3: 2.46 sec per loop


















































# looping over a collection/list
# In C
for i in xrange(len(text)):
    print text[i]


















































# In C
for i in xrange(len(text)):
    print text[i]


# In Python it's faster to
for word in text:
    print word


















































for i in xrange(1000):
    with open('sample.txt', 'w') as f:
        for i in xrange(len(text)):
            f.write(text[i])
# 72004 function calls in 0.230 seconds,


for i in xrange(1000):
    with open('sample.txt', 'w') as f:
        for word in text:
            f.write(word)
# 70004 function calls in 0.209 seconds


















































# # looping backwards
# In C
for i in xrange(len(text)-1, -1, -1):
    print text[i]


















































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

















































# looping over a collection and indicies

# in C
for i in xrange(len(text)):
    print i, '-->', text[i]

















































# in C
for i in xrange(len(text)):
    print i, '-->', text[i]


# # if manipulating indicies directly, it's probably wrong
# In Python
for i, word in enumerate(text):
    print i, '-->', word


















































for count in xrange(2000):
    with open('sample.txt', 'w') as f:
        for i in xrange(len(text)):
            line = '{0} --> {1}'.format(i, text[i])
            f.write(line)
# 844004 function calls in 0.902 seconds


for count in xrange(2000):
    with open('sample.txt', 'w') as f:
        for i, word in enumerate(text):
            line = '{0} --> {1}'.format(i, word)
            f.write(line)
#  842004 function calls in 0.873 seconds

















































# looping over two collections
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
	print names[i], '-->', colors[i]

















































# looping over two collections
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

# In C
n = min(len(names), len(colors))
for i in range(n):
	print names[i], '-->', colors[i]


# in python
for name, color in zip(names, colors):
	print name, '-->', color





















































# looping over two collections
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
	print names[i], '-->', colors[i]

# in python
for name, color in zip(names, colors):
	print name, '-->', color


# in modern processor
# not fitting in L1 cache
for name, color in izip(names, colors):
	print name, '-->', color
# izip creates an iterator over the list, generating the values one by one
















































# looping in sorted order
colors = ['red', 'green', 'blue', 'yellow']

for color in sorted(colors):
	print color

















































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
















































# Dictionary skills

# looping over the keys
d = ['matthew': 'blue', 'rachel': 'green', 'raymond':'red']

for k in d:
	print k

















































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


















































for elem in lst:
    # mutate list in place
# You should rather change it to

for elem in lst[:]:
    # mutate list in place

















































# Dictionary skills

# looping over the keys
d = ['matthew': 'blue', 'rachel': 'green', 'raymond':'red']

for k in d:
	print k

# another way
for k in d.keys():
	if k.startswith('r'):
		del[k]

# this should be done when the dictionary is mutated
# one should never mutate something while iterating over it, in any language

# d.keys() makes a copy of the list and stores it in a list
# the dictionary can be mutated

# even better
d = {k : d[k] for k in d if not k.startswith('r')}

















































# looping over dictionary keys and values

for k in d:
	print k, '-->', d[k]


















































# looping over dictionary keys and values
for k in d:
	print k, '-->', d[k]
# not fast because it has to rehash every key and do a lookup on it

# a better way
for k, v in d.items():
	print k, '-->', v

















































# looping over dictionary keys and values
for k in d:
	print k, '-->', d[k]


# a better way
for k, v in d.items():
	print k, '-->', v
# tuple unpacking, no lookups involved

for k, v in d.iteritems():
	print k, '-->', v
















































# Counting with dictionaries

names = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}
for name in names:
	if name not in d:
		d[name] = 0
	d[name] += 1
{'blue': 1, 'green': 2, 'red': 3}



















































# Counting with dictionaries
# names = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}
for name in names:
	if name not in d:
		d[name] = 0
	d[name] += 1
{'blue': 1, 'green': 2, 'red': 3}


# a better way
d = {}
for name in names:
	d[name] = d.get(name, 0) + 1

















































# Counting with dictionaries




names = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}
for name in names:
	if name not in d:
		d[name] = 0
	d[name] += 1
{'blue': 1, 'green': 2, 'red': 3}

# a better way
d = {}
for name in names:
	d[name] = d.get(name, 0) + 1

# a better way
d = defaultdict(int)
for name in names:
	d[name] += 1

















































# grouping with dictionaries
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

d = {}
for name in names:
	key = len(name)
	if key not in d:
		d[key] = []
	d[key].append(name)


















































# grouping with dictionaries
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

d = {}
for name in names:
	key = len(name)
	if key not in d:
		d[key] = []
	d[key].append(name)

# a better way
d = {}
for name in names:
	key = len(name)
	d.setdefault(key, []).append(name)	

















































# grouping with dictionaries
names = ['raymond', 'rachel', 'matthew', 'roger',
         'betty', 'melissa', 'judith', 'charlie']

d = {}
for name in names:
	key = len(name)
	if key not in d:
		d[key] = []
	d[key].append(name)

# a better way
d = {}
for name in names:
	key = len(name)
	d.setdefault(key, []).append(name)

# a better way
d = defaultdict(list)
for name in names:
	key = len(name)
	d[key].append(name)

















































# Construct a dictionary from pairs
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(izip(names, colors))
{'matthew': 'blue', 'rachel': 'green', 'raymond': 'red'}


















































# Linking dictionaries
defaults = {'color':'red', 'user':'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('=c', '--color')
namespace = parser.parse_args([])
command_line_args = {k:v for k, v in 
					 vars(namespace).items() if v}


d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)





















































# Linking dictionaries
defaults = {'color':'red', 'user':'guest'}
parser = argparse.ArgumentParser()
parser.add_argument('-u', '--user')
parser.add_argument('=c', '--color')
namespace = parser.parse_args([])
command_line_args = {k:v for k, v in 
					 vars(namespace).items() if v}


# the default way to do it
d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)


# a better way
d = ChainMap(command_line_args, os.environ, defaults)
# python3
# it links them all together

















































# Distinguishing multiple exit points in loops


def find(seq, target):
	found = False
	for i, value in enumerate(seq):
		if value == target:
			found = True
			break
	if not found:
		return -1
	return i



















































# Distinguishing multiple exit points in loops

def find(seq, target):
	found = False
	for i, value in enumerate(seq):
		if value == target:
			found = True
			break
	if not found:
		return -1
	return i

# a better way, the else clause
def find(seq, target):
	for i, value in enumerate(seq):
		if value == target:
			break
	else:
		return -1
	return i

