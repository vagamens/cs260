import unittest
from marbleBag import MarbleBag
from marble import Marble

class MarbleBagTests(unittest.TestCase):

	def test_default(self):
		mb = MarbleBag()
		self.assertEqual(mb.getMarbles(), [None, None, None, None, None, None, None, None, None, None])
		self.assertEqual(mb.getColor(), "brown")

	def test_addMarble(self):
		mb = MarbleBag()
		mb.addMarble(Marble())
		marbs = mb.getMarbles()
		for i in range(len(marbs)):
			with self.subTest():
				pass

		with self.subTest():
			marbs = mb.getMarbles()
			self.assertIsInstance(marbs[0], Marble)
			for i in range(1,len(marbs)):
				self.AssertEqual(marbs[i], None)
		#self.assertEqual(mb.getMarbles(), [type(Marble()), None, None, None, None, None, None, None, None, None])

	def test_getMarble(self):
		mb = MarbleBag()
		mb.addMarble(Marble())
		self.assertIsInstance(mb.getMarble(1), Marble)

	def test_getRandomMarble(self):
		mb = MarbleBag()
		mb.randomFillBag()

class MarbleTests(unittest.TestCase):

	def test_defaut(self):
		m = Marble()
		self.assertEqual(m.getSize(), 5)
		self.assertEqual(m.getColor(), "red")

if __name__ == '__main__':
	unittest.main()