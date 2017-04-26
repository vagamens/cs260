#!/bin/env python3

# Assignment 3:
# 	Create an array or linked list that allows adding and removing
#	from any position.

from SmartArray import SmartArray

def main():
	sa = SmartArray()
	for i in range(0, 50):
		sa.append(i)
	print(sa)
	sa.insert(10, 5)
	print(sa)

if __name__ == '__main__':
	main()