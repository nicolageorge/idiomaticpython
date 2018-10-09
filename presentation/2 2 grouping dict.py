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
