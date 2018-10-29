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
# The reason to why you should never modify a list while iterating over it is for example, 
# you're iterating over a list of 20 digits, and if you hit an even number you pop it off
# the list and carry on till you have a list of just odd numbers.

# Now, say this is your sample data [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 
# and you start iterating over it. First iteration, and the number is 1 so you continue, 
# the following number is 2 so you pop it off, and rinse and repeat. You now feel the application
 # worked correctly as the resultant list is [1, 3, 5, 7, 9, 11, 13, 15, 17, 19].

# Now let's say your sample data is [1, 2, 4, 5, 7, 8, 10, 11, 12, 13, 15, 15, 17, 18, 20]
# and you run the same piece of code as before and mutate the original list while iterating
# through it. Your resultant list is [1, 4, 5, 7, 10, 11, 13, 15, 15, 17, 20] 
# which is clearly incorrect as there are still even numbers contained in the list.

# If you are planning on mutating the list while iterating through it like so

# for elem in lst:
#     # mutate list in place
# You should rather change it to

# for elem in lst[:]:
#     # mutate list in place
# The [:] syntax creates a new list that is an exact copy of the original list, 
# so that you can happily mutate the original list without affecting what you're 
# processing as you won't have any unintended side-effects from mutating the list you're iterating through.

# If your list is rather sizable, instead of creating a new list and stepping 
# through it look at using generator expressions or write your own generator for 
# your list if you feel the need so that you do not waste memory and CPU cycles.

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

## TUPLE UNPACKING

# a better way, because items() produces a big huge list, we have iteritems()
for k, v in d.iteritems():
	print k, '-->', v
# iteritems() returns an iterator so it can be fed to all the things
# Barry Warsaw
