from random import randint


def insertion_sort(items):
	# items = ite[:]
	for i, item in enumerate(items):
		key = i-1
		while key>-1 and items[key]>item:
			items[key+1] = items[key]
			key = key-1
		items[key+1] = item
	return items


def merge_sort(items):
	if len(items) == 1:
		return items

	mid = len(items) // 2
	left = merge_sort(items[:mid])
	right = merge_sort(items[mid:])
	return merge(left, right)


def merge(left, right):
	i, j, answer = 0, 0, []

	l_len = len(left) if left is not None else 0
	r_len = len(right) if right is not None else 0

	while i<l_len and j<r_len:
		if left[i] < right[j]:
			answer.append(left[i])
			i += 1
		else:
			answer.append(right[j])
			j += 1

	if i<l_len:
		answer.extend(left[i:])
	if j<r_len:
		answer.extend(right[j:])
	return answer

if __name__ == '__main__':
	a = [randint(1, 10000) for _ in range(10000)]

	ins_sorted_a = insertion_sort(a)
	merge_sorted_a = merge_sort(a)
	sorted_a = sorted(a)

	if ins_sorted_a == sorted_a:
		print("Insertion sort worked ok")
	else:
		raise Exception("Insertion sort is bullshit")

	if merge_sorted_a == sorted_a:
		print("Merge sort worked ok")
	else:
		import pdb
		pdb.set_trace()
		raise Exception("Merge sort is bullshit")




