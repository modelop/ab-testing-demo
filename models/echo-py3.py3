import sys as sys

def action(datum):
	sys.stdout.flush()
	print(datum)
	
	yield(datum)