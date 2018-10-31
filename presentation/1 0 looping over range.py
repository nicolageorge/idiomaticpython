# looping over a range of numbers

for i in [0, 1, 2, 3, 4, 5]:
    print i**2

# python's for is not like other language "for", probably should be named foreach
# it loops over collections, using the iterator protocol
# not like the for in C

# Since you can attempt to iterate over any object,
# Python doesn't necessarily know how to iterate over whatever you've given it.
# Given a list of things it tries to do to work out how to present the values one-by-one.
# The first thing it does is checks for an __iter__ method on the object and -- if it exists -- calls it.

# The result of this call will then be an iterable object; that is, one with a next method.
# Now we're good to go: just call next repeatedly until StopIteration is raised.

# a better way
for i in range(6):
    print i**2
# they do the same thing in exactly the same way
# range produces the same list and the for loops over the list
# range 1000000 equals quite a big list, estimated 32mb of memory
# for list only

# better way, XRANGE
for i in xrange(6):
    print i**2
# produces an iterator over the range, giving the values one at a time
# xrange is better and also ugly


# python3
# range was replaced with xrange
# beautiful is better than ugly

# /usr/bin/python2.7 -m timeit '"-".join([str(n) for n in xrange(1000000)])'
# 10 loops, best of 3: 263 msec per loop
# /usr/bin/python2.7 -m timeit '"-".join([str(n) for n in range(1000000)])'
# 10 loops, best of 3: 272 msec per loop

# /usr/bin/python2.7 -m timeit '"-".join([str(n) for n in range(10000000)])'
# 10 loops, best of 3: 2.58 sec per loop
# /usr/bin/python2.7 -m timeit '"-".join([str(n) for n in xrange(10000000)])'
# 10 loops, best of 3: 2.46 sec per loop
