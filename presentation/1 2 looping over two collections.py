# looping over two collections
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

# take the length of the shorter list, loop over indicies
# until the ith element
n = min(len(names), len(colors))
for i in range(n):
    print names[i], '-->', colors[i]

# in python
for name, color in zip(names, colors):
    print name, '-->', color
# to loop over this, we manifest a third list in memory
# that consists of tuples, each of it consists of separate objects
# with pointers back to the original
# it takes far more memory than
# orig 2 lists combined, it doesn't scale


# in modern processor
# not fitting in L1 cache
# code should be running in L1 cache
# on cache miss a simple move goes from 1 clockcycle to 400-600
# clock cycles, losing 2 oreders of magnitude
for name, color in izip(names, colors):
    print name, '-->', color
# izip creates an iterator over the list, generating the values one by one
# iterators were done by Guido
