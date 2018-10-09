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

