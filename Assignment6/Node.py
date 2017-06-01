class Node(object):
	"""docstring for Node"""
	def __init__(self, value=None):
		self.arg = arg
		self.value = value
		self.count = 0
		self.left = None
		self.right = None
		self.parent = None
	
	def add(self, val):
		if self.value == None:
			self.value = val
		elif val > self.value:
			if self.right == None:
				self.right = Node(val)
			else:
				self.right.add(val)
		elif val < self.value:
			if self.left == None:
				self.left = Node(val)
			else:
				self.left.add(val)
		else:
			self.count+=1;

	def getNode(self, val):
		if self.value == val:
			return self
		elif val > self.value:
			return self.right.getNode(val)
		elif val < self.value:
			return self.left.getNode(val)

	def getValue(self):
		return self.value

	def setValue(self, val):
		self.value = val

	def getLeft(self):
		return self.left

	def setLeft(self, node):
		self.left = node

	def getRight(self):
		return self.right

	def setRight(self, node):
		self.right = node

	def getParent(self):
		return self.parent

	def setParent(self, node):
		self.parent = node

	def preOrderTraversal(self):
		order = []
		if(self.left != None):
			order = self.left.preOrderTraversal()
		if(right != None):
			for v in self.right.preOrderTraversal():
				order.append(v)
		order.insert(0, self.value)
		return order

	def inOrderTraversal(self):
		order = []
		if(self.left != None):
			order = self.left.inOrderTraversal()
		order.append(self.value)
		if(self.right != None):
			for v in self.right.inOrderTraversal():
				order.append(v)
		return order

	def postOrderTraversal(self):
		order = []
		if(self.left != None):
			order = self.left.postOrderTraversal()
		if(self.right != None):
			for v in self.right.postOrderTraversal():
				order.append(v)
		order.append(self.value)
		return order