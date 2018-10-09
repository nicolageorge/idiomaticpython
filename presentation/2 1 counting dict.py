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
