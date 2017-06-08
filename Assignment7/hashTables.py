import sys
sys.path.insert(0, '../Assignment2')
from LinkedList import LinkedList

class DumbHashTable(object):
	"""docstring for DumbHash"""
	def __init__(self, arg):
		super(DumbHash, self).__init__()
		self.arg = arg
		self.table = []

	def add(self, value):
		keyPair = self.hash(value)
		if keyPair[0] > len(self.table):
			for x in range((keyPair - len(self.table))):
				self.table.append(0)
		self.table[keyPair[0]] = keyPair[1]

	def getHash(self, value):
		keyPair = self.hash(value)
		return self.table[keyPair[0]]

	@staticmethod
	def hash(value):
		# essentially does a rot13 cypher
		newValue = DumbHashTable.caesar(value, 13)
		key = 0
		for ch in newValue:
			key+=ord(ch)
		return (key, newValue)

	@staticmethod
	def caesar(plainText, shift):
		cypherText = ''
		for ch in plainText:
			if ch.isalpha():
				stayInAlphabet = ord(ch) + shift
				if stayInAlphabet > ord('z'):
					stayInAplhabet -= 26
				finalLetter = chr(stayInAlphabet)
			cypherText += finalLetter

		print 'Your cyphertext is: ', cyphertext

		return cyphertext

class SmartHashTable(object):
	"""docstring for SmartHashTable"""
	def __init__(self, arg):
		super(SmartHashTable, self).__init__()
		self.arg = arg
		self.table = []

	def add(self, value):
		keyPair = DumbHashTable.hash(value)
		if keyPair[0] > len(self.table):
			for x in range((keyPair - len(self.table))):
				self.table.append(LinkedList)
		self.table[keyPair[0]].append(keyPair[1])