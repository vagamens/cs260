#!/bin/env python3

import os
import sys

def help():
	return "Help Page"

def flatten(l):
	newList = []
	for i in range(len(l)):
		if('list' in str(type(l[i]))):
			temp = flatten(l[i])
			for j in range(len(temp)):
				newList.append(temp[j])
		else:
			newList.append(l[i])
	return newList

def buildHeader(head):
	header = []
	header = head.split('{');
	header = flatten(header)
	newHead = []
	for i in range(len(header)):
		if('}' in header[i]):
			newHead.append(flatten(header[i].split('}')))
		else:
			newHead.append(header[i])
	header = flatten(newHead)
	return header

def parseEscape(head):
	head[2] = head[2].split('\\n')
	h2 = ''
	for i in range(len(head[2])-1):
		h2 = head[2][i] + '\n'
	head[2] = h2 + head[2][-1]
	head[2] = head[2].split('\\t')
	h2 = ''
	for i in range(len(head[2])-1):
		h2 = head[2][i] + '\t'
	head[2] = h2 + head[2][-1]
	return head

def parseHeader(header, curval, vals):
	head = buildHeader(header)
	head = parseEscape(head)
	h = ''
	if(vals['filetype'] == 'py'):
		h = h + "#/bin/env python"
		if(vals['filetype'] == 3):
			h = h + '3'
	h = h + '\n\n'
	for i in range(len(head)):
		if(head[i] == '%num%'):
			h = h + str(curval)
		else:
			h = h + head[i]
	return h

def assignmentName(assignment, curval):
	return assignment + ' ' + str(curval)

def fileName(filetype):
	fName = ''
	if (filetype == 'py'):
		fName = 'main.py'
	return fName

def location(assignment, fName, curval):
	return assignmentName(assignment, curval) + '/' + str(fName)

def main(args):
	vals = {'begin':1, 'filetype':'py'}
	if len(args) == 1:
		print(help())
	else:
		args = args[1:]
		for i in range(len(args)):
			if('-' in args[i]):
				if(args[i] == '-b' or args[i] == '--begin'):
					try:
						vals['begin'] = int(args[i+i])
					except:
						print(help())
				elif(args[i] == '-e' or args[i] == '--end'):
					try:
						vals['end'] = int(args[i+1])
					except:
						print(help())
				elif(args[i] == '-a' or args[i] == '--assignment'):
					vals['assignment'] = args[i+1]
				elif(args[i] == '-f' or args[i] == '--filetype'):
					vals['filetype'] = args[i+1]
				elif(args[i] == '-h' or args[i] == '--header'):
					vals['header'] = args[i+1]
				elif(args[i] == '--fileversion'):
					vals['version'] = int(args[i+1])
		for i in range(vals['begin'], vals['end']+1):
			aName = fileName(vals['filetype'])
			loc = location(vals['assignment'], aName, i)
			header = parseHeader(vals['header'], i, vals)
			print('\n')
			print(loc)
			print(header)
			try:
				os.mkdir(loc.split('/')[0])
				os.system('touch '+loc)
				os.system('cat "'+header+'" > "'+loc+'"')
			except:
				pass

if __name__ == '__main__':
	main(sys.argv)