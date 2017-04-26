from Node import Node
from Node import HeadNode, TailNode

class LinkedList(object):
	"""docstring for LinkedList"""
	def __init__(self, arg):
		super(LinkedList, self).__init__()
		self.arg = arg
		self.head = HeadNode(None)
		self.tail = TailNode(self.head)
		self.head.setAdjacent(self.tail)

	def appendNode(self, value):
		node = Node(None, None, value)
		self.tail.previous.setAdjacent(node)
		self.tail.setPrevious(node)

	def append(self, value):
		self.appendNode(value)

	def popNode(self, pos):
		if(pos >= 0):
			value = self.head.getValue(pos)
			node = self.head.getNode(pos)
			node.previous.setAdjacent(node.next)
			node.next.setPrevious(node.previous)
			return value
		else:
			value = self.tail.getValue(pos)
			node = self.tail.getNode(pos)
			node.previous.setAdjacent(node.next)
			node.next.setPrevious(node.previous)
			return value

	def pop(self, pos):
		return self.popNode(pos)

	def getNodeValue(self, pos):
		return self.head.getValue(pos)
