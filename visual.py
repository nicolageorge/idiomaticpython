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
















































# looping over a collection/list

# In C
for i in xrange(len(text)):
    print text[i]


# In Python it's faster to
for word in text:
    print word
















































# looping over a collection/list

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
























































# looping over a collection and indicies

# in C
for i in xrange(len(text)):
    print i, '-->', text[i]















































# looping over a collection and indicies

# in C
for i in xrange(len(text)):
    print i, '-->', text[i]


# In Python
for i, word in enumerate(text):
    print i, '-->', word
















































# looping over a collection and indicies

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
names = ['andrei', 'luis', 'cristi']
colors = ['rosu', 'verde', 'albastru', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
    print names[i], '-->', colors[i]

















































# looping over two collections
names = ['andrei', 'luis', 'cristi']
colors = ['rosu', 'verde', 'albastru', 'yellow']

# In C
n = min(len(names), len(colors))
for i in range(n):
    print names[i], '-->', colors[i]


# in python
for name, color in zip(names, colors):
    print name, '-->', color

























# looping over two collections
names = ['andrei', 'luis', 'cristi']
colors = ['rosu', 'verde', 'albastru', 'yellow']

# In C
n = min(len(names), len(colors))
for i in range(n):
    print names[i], '-->', colors[i]


# in python
for name, color in zip(names, colors):
    print name, '-->', color

# better
for name, color in izip(names, colors):
    print name, '-->', color








































# Functions which consume Iterators

# Looping Backwards

# In C
for i in xrange(len(text)-1, -1, -1):
    print text[i]


# In Python
for word in reversed(text):
    print word












































# Functions which consume Iterators

# looping in sorted order
colors = ['rosu', 'verde', 'albastru', 'yellow']

for color in sorted(colors):
    print color


















































# looping in sorted order
colors = ['rosu', 'verde', 'albastru', 'yellow']

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

names = ['tudor', 'gabriel', 'catalina', 'alin']

def compare_length(c1, c2):
    if len(c1) < len(c2): return -1
    if len(c1) > len(c2): return 1
    return 0

print sorted(names, cmp=compare_length)
# on 1 000 000, Nlog(N) comparations - 20 000 000 comparations

# a better way
print sorted(names, key=len)
# called once per key, on 1 000 000, called 1 000 000 times



















































blocks = []
while True:
    block == f.read(32)
    if block == '':
        break
    blocks.append(block)








































# a sentinel value

blocks = []
while True:
    block == f.read(32)
    if block == '':
        break
    blocks.append(block)

# this code does the same thing
blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)







































# Dictionary skills

# looping over the keys
d = ['Alina': 'albastru', 'Cristi': 'verde', 'Gabriel':'rosu']

for k in d:
    print k




















































# Dictionary skills

# looping over the keys
d = ['Alina': 'albastru', 'Cristi': 'verde', 'Gabriel':'rosu']

for k in d:
    print k

# another way
for k in d.keys():
    if k.startswith('r'):
        del[k]
































































# Dictionary skills

# looping over the keys
d = ['Alina': 'albastru', 'Cristi': 'verde', 'Gabriel':'rosu']

for k in d:
    print k

# another way
for k in d.keys():
    if k.startswith('r'):
        del[k]


for elem in lst:
    # mutate list in place
# You should rather change it to

for elem in lst[:]:
    # mutate list in place

# same with dictionaries

































































































# Dictionary skills

# looping over the keys
d = ['matthew': 'albastru', 'rachel': 'verde', 'raymond':'rosu']

for k in d:
    print k

# another way
for k in d.keys():
    if k.startswith('r'):
        del[k]

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

names = ['Andrei', 'Luis', 'Andrei', 'Irina', 'Tudor', 'Vadim', 'Vlad',
         'Tudor', 'George', 'Nicu','Cristi', 'Alina', 'Vlad', 'Andrei',
         'Gabriel', 'Alin', 'Cristi', 'Catalina', 'Alex', 'Gabriel',
         'Vic', 'Alin', 'Andra', 'Cristina', 'Alina', 'Alex', 'Alex', 'Radu',

d = {}
for name in names:
    if name not in d:
        d[name] = 0
    d[name] += 1
{'Cristi': 2, 'Vlad': 2, 'Vadim': 1, 'Catalina': 1, 'Alex': 3, 'Alin': 2,
 'Tudor': 2, 'Gabriel': 2, 'Cristina': 1, 'Irina': 1, 'Alina': 2, 'Nicu': 1,
 'Radu': 1, 'Andrei': 3, 'Andra': 1, 'Luis': 1, 'Vic': 1, 'George': 1}



















































# Counting with dictionaries
names = ['Andrei', 'Cristi', 'Alina', 'Andrei', 'Andrei', 'Cristi']

d = {}
for name in names:
    if name not in d:
        d[name] = 0
    d[name] += 1


# a better way
d = {}
for name in names:
    d[name] = d.get(name, 0) + 1

{'Cristi': 2, 'Alina': 1, 'Andrei': 3}















































# Counting with dictionaries
names = ['Andrei', 'Cristi', 'Alina', 'Andrei', 'Andrei', 'Cristi']

d = {}
for name in names:
    if name not in d:
        d[name] = 0
    d[name] += 1

# a better way
d = {}
for name in names:
    d[name] = d.get(name, 0) + 1

# a better way
d = defaultdict(int)
for name in names:
    d[name] += 1

{'Cristi': 2, 'Alina': 1, 'Andrei': 3}
















































# grouping with dictionaries
names = ['Andrei', 'Luis', 'Andrei', 'Irina', 'Tudor', 'Vadim', 'Vlad',
         'Tudor', 'George', 'Nicu','Cristi', 'Alina', 'Vlad', 'Andrei',
         'Gabriel', 'Alin', 'Cristi', 'Catalina', 'Alex', 'Gabriel',
         'Vic', 'Alin', 'Andra', 'Cristina', 'Alina', 'Alex', 'Alex', 'Radu']

d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)

{3: ['Vic'], 
 4: ['Luis', 'Vlad', 'Nicu', 'Vlad', 'Alin', 'Alex', 'Alin', 'Alex', 'Alex', 'Radu'], 
 5: ['Irina', 'Tudor', 'Vadim', 'Tudor', 'Alina', 'Andra', 'Alina'], 
 6: ['Andrei', 'Andrei', 'George', 'Cristi', 'Andrei', 'Cristi'], 
 7: ['Gabriel', 'Gabriel'], 
 8: ['Catalina', 'Cristina']}

















































# grouping with dictionaries
names = ['Andrei', 'Cristi', 'Vic', 'Gabriel',
         'Alina', 'Luis', 'Tudor', 'Alex']

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

{3: ['Vic'], 
 4: ['Luis', 'Alex'], 
 5: ['Alina', 'Tudor'], 
 6: ['Andrei', 'Cristi'], 
 7: ['Gabriel']}

















































# grouping with dictionaries
names = ['Andrei', 'Cristi', 'Vic', 'Gabriel',
         'Alina', 'Luis', 'Tudor', 'Alex']

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
names = ['Alina', 'Catalina', 'Cristi']
colors = ['rosu', 'verde', 'albastru']

d = dict(izip(names, colors))
{'Cristi': 'albastru', 'Alina': 'rosu', 'Catalina': 'verde'}


















































# Linking dictionaries
defaults = {'color':'rosu', 'user':'guest'}
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
defaults = {'color':'rosu', 'user':'guest'}
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