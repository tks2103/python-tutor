'''
In this class, you will implement a Node from scratch. You will then use your Node to create a list structure containing data given to you in an array. You will finally iterate over your list of Nodes to print the data. You will have 25 minutes.

A node is an object that contains some data, and a point to another node object.
Your node should implement the following functions:
	Constructor : (data, ptr)
		Creates a new Node containing 'data' and pointing to another node 'ptr'
	getNext: ()
		Returns a pointer to the next Node
	getData: ()
		Returns the value of data
	setNext: (ptr)
		Sets the value of the next Node to ptr
	setData: (data)
		Sets the value of the data to 'data'

'''

class Node:

'''
After implementing the Node, create a list of linked Nodes containing the data in the array 'ary'. Your output should be a single Node, head_node, which is the first Node in a list of linked Nodes representing each element of 'ary'. 
'''

ary = [3,12,3,42,1111]

'''
After reading in the elements of 'ary' into a list of linked Nodes, you will now print them out. Iterate over your Nodes and print their data elements. DO NOT ITERATE OVER THE ARRAY ARY OR USE THE LENGTH OF ARY TO HELP YOU PRINT.
'''

#printing code here

'''
You are complete! Running your code should produce the following input:

3
12
3
42
1111
'''
