def sort(array):
	narray = [x for x in array]
	tree = createTree(narray)
	return tree.traverse()

def createTree(array):
	tree = Tree(array.pop(len(array)/2))
	for i in array:
		tree.insert(i)
	return tree

class Node(object):
	"""docstring for Node"""
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None

	def getValue(self, value):
		return self.value

	def insert(self, node):
		if node.value <= self.value:
			if self.left == None:
				self.left = node
			else:
				self.left.insert(node)
		else:
			if self.right == None:
				self.right = node
			else:
				self.right.insert(node)

	def traverse(self):
		order = []
		if(self.left != None):
			order = self.left.traverse()
		order.append(self.value)
		if(self.right != None):
			for v in self.right.traverse():
				order.append(v)
		return order
		

class Tree(object):
	"""docstring for Tree"""
	def __init__(self, rootValue=None):
		self.root = Node(rootValue)
		
	def insert(self, value):
		node = Node(value)
		self.root.insert(node)

	def traverse(self):
		return self.root.traverse()