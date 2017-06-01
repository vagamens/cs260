from Node import Node

class Tree(object):
	"""docstring for Tree"""
	def __init__(self):
		self.arg = arg
		self.root = Node()

	def insert(selfvalue):
		self.root.add(value)

	def preOrderTraversal(self):
		return self.root.preOrderTraversal()

	def inOrderTraversal(self):
		return self.root.inOrderTraversal()

	def postOrderTraversal(self):
		return self.root.postOrderTraversal()

	def breadthFirst(self):
		stack = []
		order = []
		stack.append(self.root)
		for node in stack:
			stack.append(node.left)
			stack.append(node.right)
			order.append(node.getValue())
		return order

	def __str__():
		pass
