# Distinguishing multiple exit points in loops
# Donald Knuth came up with some structured equivalent
# need flag variable to say if something is found or not found
# the code could be returned/exited earlier when value is found, however this type of code is 
# usually a portion of a bigger functionality thus can't be exited early
def find(seq, target):
	found = False
	for i, value in enumerate(seq):
		if value == target:
			found = True
			break
	if not found:
		return -1
	return i

# a better way, the else clause
# basically, the for loop says:
# if loop not finished, keep doing the body
# if loop not finished, keep doing the body
# if body finished and no break was encountered - else
# so se can have an else clause, it's associated with if
# else should be called nobreak
# if it sould have that name, everybody would use it properly
def find(seq, target):
	for i, value in enumerate(seq):
		if value == target:
			break
	else:
		return -1
	return i
# in the future,
# emphasis on why it should be called no break
# two ways to exit the loop:
# 	finish it normally
# 	break out
# search your house for the keys, two outcomes
# 	find the keys
# 	searched all the rooms and didn't find
# if finished the loop and didn't encounter a break, do else
# should be called no break and everybody would know what it does
# just like if lambda would be called makefunction
# nobody would ask what lambda does anymore
