class BSTNode(object):
	def __init__(self, parent, k):
		self.key = k
		self.parent = parent
		self.left = None
		self.right = None

	def find(self, k):
		if k == self.key:
			return self
		elif k < self.key:
			if self.left is None:
				return None
			else:
				return self.left.find(k)
		else:
			if self.right is None:
				return None
			else:
				return self.right.find(k)

	def find_min(self):
		current = self
		while current.left is not None:
			current = current.left
		return current

	def next_larger(self):
		if self.right is not None:
			return self.right.find_min()
		
		current = self
		while current.parent is not None and current is current.parent.right:
			current = current.parent
		return current.parent

	def insert(self, node):
		if node is None:
			return

		if node.key < self.key:
			if self.left is None:
				node.parent = self
				self.left = node
			else:
				self.left.insert(node)
		else:
			if self.right is None:
				node.parent = self
				self.right = node
			else:
				self.right.insert(node)

	def delete(self, node):
		if self.left or self.right is None:
			if self is self.parent.left:
				self.parent.left = self.left or self.right
				if self.parent.left is not None:
					self.parent.left.parent = parent
			else:
				self.parent.right = self.left or self.right
				if self.parent.right is not None:
					self.parent.right.parent - parent
		else:
			s = self.next_larger()
			s.key, self.key = self.key, s.key
			return s.delete()


class BST(object):
	def __inti__(self):
		self.root = None

	def find(self, k):
		return self.root and self.root.find(k)

	def insert(self, k):
		node = BSTNode(None, k)
		if self.root is None:
			if self.root = node
		else:
			self.root.insert(node)

	def delete(self, k):
		node = self.find(k)

		if node is None:
			return None
		if node is self.root:
			pseudoroot = BSTNode(None, 0)
			pseudoroot.left = self.root
			self.root.parent = pseudoroot
			deleted = self.root.delete()
			self.root = pseudoroot.left
			if self.root is not None:
				self.root.parent = None
			return deleted
		else:
			return node.delete()

	def next_larger(self, k):
		node = self.find(k)
		return node and node.next_larger()




