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






















































