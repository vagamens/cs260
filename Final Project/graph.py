class Graph(object):
	"""docstring for Graph"""
	def __init__(self):
		self.graph = dict()

	def addNode(name):
		self.graph[name] = dict()

	def addEdge(node1, node2, weight):
		if(node1 in self.graph and node2 in self.graph):
			self.graph[node1][node2] = weight
			self.graph[node2][node1] = weight
		elif (node1 not in self.graph and node2 not in self.graph):
			print node1 + " and " + " are not in the graph."
			print "please add them before attemping to create this edge."
		elif (node1 not in self.graph):
			print node1 + " is not in the graph."
			print "Please create it before attempting to create this edge."
		elif (node2 not in self.graph):
			print node1 + " is not in the graph."
			print "Please create it before attempting to create this edge."

	def getMinimumWeight(start, dest):
		'''
			Where start is the node you are starting at
			and dest is your destination node.
			If you get zero, you have done something wrong.
		'''
		weights = []
		if(start not in self.graph and dest not in self.graph):
			return 0
		if(start == dest):
			return 0
		for node in self.graph:
			weight = 0
			if(node == dest):
				continue
			if(dest in node):
				weight += getMinimumWeight(start, node)
			weights.append(weight)
		weights.sort()
		for i in weights:
			if i == 0:
				continue
			return i