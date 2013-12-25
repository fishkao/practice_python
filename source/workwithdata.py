#!/usr/bin/python

def basic_operation_on_list():
	"""
	- is not supported in list operations
	"""
	print "generate for range(4)", range(4)
	print "get the length of a list", range(3)
	
	a = [-3,-2,-1,0,1,2,3]
	b = [4,5]
	c = [2,3,4]
	print "+ * on list:", a+b, b*3

	print "get list element:", a[0]

	print "sub list:", a[1:-2], a[1:-2:1]

	print "slice indices:", a[0:6:1], a[0:6:2]

	print "reverse list by slice indices:", a[::-1]



def sum(a_list):
	"""
	>>> sum([1,2,3])
	6
	"""
	result = 0
	for i in a_list:
		result += i
	return result

def sum_str(a_list):
	"""
	>>> sum_str(["aa","bb","cc"])
	'aabbcc'
	"""
	result = ''
	for i in a_list:
		result += i
	return result

def cumulative_sum(a_list):
	"""
	>>> cumulative_sum([1,2,3])
	[1, 3, 6]
	"""
	if not a_list or len(a_list)<=0:
		return 0
	result = []
	tmp = 0
	for i in a_list:
		tmp += i
		result.append(tmp)
	return result

def list_sort(a_list):
	"""
	>>> a = [[2, 3], [4, 6], [6, 1]]
	>>> a.sort(key=lambda x: x[1])
	>>> a
	[[6, 1], [2, 3], [4, 6]]
	"""
	a.sort(key=lambda x:x[1])

'''
Returns an iterator of tuples, where the i-th tuple 
contains the i-th element from each of the argument 
sequences or iterables. The iterator stops when the 
shortest input iterable is exhausted. With a single
iterable argument, it returns an iterator of 
1-tuples. With no arguments, it returns an empty 
iterator. 
'''
def izip(*iterables):
	iterables = map(iter,iterables)
	while iterables:
		yield tuple(map(next,iterables))

def sort_list_reverse(a_list):
	print sorted(a_list,reverse=True)





if __name__ == "__main__":
	basic_operation_on_list()
	import doctest
	doctest.testmod()



