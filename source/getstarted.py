#!/usr/bin/python

def pro_4(x,y):
	"""
	>>> pro_4(2,6)
	(6, 4)
	"""
	x,y = y,x+2
	return x,y


if __name__ == "__main__":
    import doctest
    doctest.testmod()
