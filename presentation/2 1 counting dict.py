# rehear raymond
# factory functions
# defaultdict vs dict
# Counting with dictionaries
# names = ['red', 'green', 'red', 'blue', 'green', 'red']
# names = ['Tudor', 'Luis', 'Alina', 'Gabriel', 'Andrei', 'George', 'Andrei']
andrei, luis, andrei, irina, tudor, tudor, vadim, vlad,
gabriel, andrei, vlad, andrei, 
names = ['Alina', 'Andrei', ]


d = {}
for name in names:
	if name not in d:
		d[name] = 0
	d[name] += 1
{'blue': 1, 'green': 2, 'red': 3}
# look up the dictionary, see if the value is there
# and if it's not, add it

# a better way
d = {}
for name in names:
	d[name] = d.get(name, 0) + 1
# get the name, if the name is missing, add 1 to the 0

# a better way
d = defaultdict(int)
for name in names:
	d[name] += 1
# factory functions
# int can be called with no argument, producing the value 0
# return a defaultdict which sometimes behaves different than dict
