class Node(object):
	"""docstring for Node"""
	def __init__(self, previous, adjacent, value, **kwargs):
		super(Node, self).__init__(**kwargs)
		self.previous = previous
		self.adjacent = adjacent
		self.value = value

	def getNode(self, pos=0):
		if(pos == 0):
			return self
		elif(pos <= 0):
			return self.previous.getNode(pos+1)
		else:
			return self.next.getNode(pos-1)

	def getValue(self, pos=0):
		if(pos <= 0):
			return self.value
		else:
			return self.previous.getValue(pos-1)

	def setValue(self, value):
		self.value = value

	def getAdjacent(self):
		return self.adjacent

	def setAdjacent(self, node):
		if ('Node' in str(type(node))):
			self.adjacent = node
		else:
			raise NotANode(node)

	def getPrevious(self):
		return self.previous

	def setPrevious(self, node):
		if ('Node' in str(type(node))):
			self.adjacent = node
		else:
			raise NotANode(node)
		

class HeadNode(Node):
	"""docstring for HeadNode"""
	def __init__(self, adjacent, **kwargs):
		super(HeadNode, self).__init__(None, adjacent, None, **kwargs)
		self.arg = arg

	def getNode(self, pos):
		if(pos == 0):
			return self.adjacent
		else:
			return self.adjacent.getNode(pos)
		
class TailNode(Node):
	"""docstring for TailNode"""
	def __init__(self, previous, **kwargs):
		super(TailNode, self).__init__(previous, None, None, **kwargs)
		self.arg = arg

	def getValue(self, pos=0):
		raise NodeDoesNotExist()

class NotANode(Exception):
	def __init__(self, notNode):
		self.notNode = notNode
	def __str__(self):
		return repr(self.notNode) + "is not a node"

class NodeDoesNotExist(Exception):
	def __init__(self):
		pass
	def __str__(self):
		return "Node not found,\nThe List is not that long."