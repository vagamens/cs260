#!/bin/env python3

# Assignment 1:
#	Make a like of properties and behaviors for a bag of marbles,
#	implement them, test the implementation in a driver class and
#	demonstrate program correctness

from marbleBag import MarbleBag
from marble import Marble

def main():
	mb = MarbleBag()
	mb.randomFillBag()
	for i in range(len(mb.getMarbles())):
		print(str(mb.getMarbles()[i]))

if __name__ == '__main__':
	main()