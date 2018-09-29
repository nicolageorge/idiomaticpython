# 	Replace traditional index manipulation with Python's core looping idioms
# when you use index searching, unless exotic circumstance, should not be doing

# 	Learn advanced techniques with for-else clauses and the two argument form of iter()

# Goal: Improve your craftmanship and aim for clean fast, idimatic Python code

# looping over a range of numbers
for i in [0, 1, 2, 3, 4, 5]:
	print i**2
# python's for is not like other language "for", probably should be named foreach
# it loops over collections, using the iterator protocol

# a better way
for i in range(6):
	print i**2
# they do the same thing in exactly the same way
# range produces the same list and the for loops over the list

# if range(1000000), 32mb memorie

# better way
for i in xrange(6):
	print i**2
# produces an iterator over the range, giving the values one at a timec

# python3
# xrange was replaced with range
