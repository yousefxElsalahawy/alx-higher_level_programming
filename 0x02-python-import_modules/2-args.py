#!/usr/bin/python3
if __name__ == "__main__":
	import sys
	n = int (len(sys.argv[1:]))

	if n > 1:
		print("{} arguments:".format(n))
		for x in range(1,n + 1):
			print("{}: {}".format(x, sys.argv[x]))
	elif n == 0:
		print("{} arguments.".format(n))
	elif n == 1:
		print("{} argument:".format(n))
		print("{}: {}".format(1, sys.argv[1]))
