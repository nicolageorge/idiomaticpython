# looping in sorted order
colors = ['red', 'green', 'blue', 'yellow']

for color in sorted(colors):
	print color

# looping over reversed sorted list
for color in sorted(colors, reverse=True):
	print color


# Custom sort order
# the classic way, by making a custom comparison function

def compare_length(c1, c2):
	if len(c1) < len(c2): return -1
	if len(c1) > len(c2): return 1
	return 0

print sorted(colors, cmp=compare_length)
# on 1 000 000, Nlog(N) comparations - 20 000 000 comparations

# a better way
print sorted(colors, key=len)
# called once per key, on 1 000 000, called 1 000 000 times
# from sql, everything is ordered but not by comparison function
# in python3 - no more comparison functions
