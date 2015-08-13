#!/usr/bin/python

import sys
import signal
import itertools
import time

def signal_handler(signal, frame):
	print('=================')
	print('Execution aborted')
	print('=================')
	sys.exit(1)


def usage ():
	print "\n\tUsage:"
	print "\tbruter.py -c <characters list> [-m <max lenght> | -f <fixed length> ]"
	exit()
	
def print_array(array):
	print array
	#for item in array:
		#print item

def max_lenght_generator(mylist, lenght):
	complete_list = []
	for current in xrange(int(lenght)):
		array = [i for i in mylist]
		for y in xrange(current):
			array = [x+i for i in mylist for x in array]
		complete_list = complete_list+array
		print_array(array)

def fixed_lenght_generator(mylist, lenght):
	complete_list = []
	for item in itertools.product(mylist, repeat=int(lenght)):
		complete_list .append(''.join(item))
	print_array(complete_list)
	
if __name__ == "__main__":
	signal.signal(signal.SIGINT, signal_handler)
	if len(sys.argv) != 5:
		usage()
	parameters = {sys.argv[1]:sys.argv[2], sys.argv[3]:sys.argv[4]}
	mylist = parameters["-c"]
	if "-m" in parameters:
		max_lenght_generator(mylist, parameters["-m"])
	elif "-f" in parameters:
		fixed_lenght_generator(mylist, parameters["-f"])
