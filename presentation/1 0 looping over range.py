# looping over a range of numbers

for i in [0, 1, 2, 3, 4, 5]:
	print i**2
# python's for is not like other language "for", probably should be named foreach
# it loops over collections, using the iterator protocol
# not like the for in C

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
