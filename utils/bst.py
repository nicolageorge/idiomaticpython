from random import randint

class BSTNode(object):
	def __init__(self, parent, val):
		self.val = val
		self.parent = parent
		self.left = None
		self.right = None


	def in_order_traversal(self, root):
	        res = []
	        if root:
	            res.append(self.in_order_traversal(root.left))
	            res.append(root.val)
	            res.extend(self.in_order_traversal(root.right))

	        import pdb
	        pdb.set_trace()
	        return res

	def find(self, val):
		if self.val == val:
			return self
		elif val < self.val:
			if self.left is None:
				return None
			else:
				return self.left.find(val)
		else:
			if self.right is None:
				return None
			else:
				return self.right.find(val)

	def find_min(self):
		curent = self
		while curent.left is not None:
			curent = curent.left
		return curent

	def next_larger(self):
		# import pdb
		# pdb.set_trace()
		if self.right is not None:
			return self.right.find_min()

		curent = self
		while self.parent is not None and self == self.parent.right:
			curent = self.parent
		return curent.parent

	def insert(self, node):
		if node is None:
			return None

		if node.val < self.val:
			if self.left is None:
				node.parent = self.left
				self.left = node
				print('node inserted to the left')
				curent = self.parent
				print('parent path')
				while curent is not None:
					print(curent.val)
					curent = curent.parent

			else:
				self.left.insert(node)
		else:
			if self.right is None:
				node.parent = self.right
				self.right = node
				print('node inserted to the right')
				curent = self.parent
				print('parent path')
				while curent is not None:
					print(curent.val)
					curent = curent.parent
			else:
				self.right.insert(node)

		# import pdb
		# pdb.set_trace()

	def delete(self, node):
		if self.left is None or self.right is None:
			if self is self.parent.left:
				self.parent.left = self.left or self.right
				if self.parent.left is not None:
					self.parent.left.parent = self.parent
			else:
				self.parent.right = self.left or self.right
				if self.parent.right is not None:
					self.parent.right.parent = self.parent
		else:
			s = self.next_larger()
			s.val, self.val = self.val, s.val
			return s.delete()


class BST(object):
	def __init__(self):
		self.root = None

	def find(self, val):
		return self.root and self.root.find(val)

	def insert(self, val):
		node = BSTNode(None, val)

		if self.root is None:
			self.root = node
		else:
			self.root.insert(node)

	def next_larger(self, val):
		node = self.find(val)
		return node and node.next_larger()

	def iot(self):
		self.root.in_order_traversal(self.root)

	def delete(self, val):
		node = self.find(val)

		if node is None:
			return None
		if node is self.root:
			pseudoroot = BSTNode(None, 0)
			pseudoroot.left = self.root
			self.root.parent = pseudoroot
			self.root.delete()
			self.root = pseudoroot.left
			if self.root is not None:
				self.root.parent = None
			return deleted
		else:
			return node.delete()


def main():
	bst = BST()
	for _ in range(100):
		bst.insert(randint(1, 10000))

	bst.iot()

if __name__ == '__main__':
	main()





