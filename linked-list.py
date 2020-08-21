"""
Linked lists are data structures consisting of chained nodes, where each 
node contains data and a pointer to the next node. In doubly linked lists 
there are pointers to the previous and next value.

A value is at the start of a linked list is called the head, with the last value being the tail.

A node is considered to be the tail if the next node property of a node is null or None.

A node is considered to be the head if the previous node property of a node is null or None. (doubly linked list only)
"""

class Node:
	def __init__(self, data,nextn,prev):
		self.data = data
		self.nextn = nextn
		self.prev = prev


# Doubly linked list
class DLinkedList: 
	def __init__(self):
		self.head = None
		self.tail = None
		self.list = []

	def initializeList(self, data):
		# Creates a doubly linked list using an input list/array of data values
		curr_node = None
		next_node = None
		return_list = []
		for i in range(len(data)):
			if i == 0: 
			# Action if the first node is being created
				curr_node = Node(data=data[i], prev=None, nextn=None)
				self.head = curr_node
				next_node = Node(data=data[i+1], prev=curr_node, nextn=None)
 				
 				# After next node is made the first node can point to it as the next in line
				curr_node.nextn = next_node 
				return_list.append(curr_node)
				curr_node = next_node
			elif i > 0:
				if i+1 == len(data): # len = 6 i = 5
					curr_node.nextn = None
					return_list.append(curr_node)
					self.tail = curr_node
					self.list = return_list
				else:
					next_node = Node(data=data[i+1],prev=curr_node, nextn=None)
					curr_node.nextn = next_node
					return_list.append(curr_node)
					curr_node = next_node
		
	def traverseList(self):
		# Shows node data and all pointers in a grid-like format
		node = self.head
		while node is not None:

			prev = node.prev
			nextn = node.nextn 
			prev_data = 0
			nextn_data = 0

			# Head prev value and Tail next value is set to none
			if node.prev != None:
				prev_data = prev.data
			
			if node.nextn != None:
				nextn_data = nextn.data

			# print(node.data, end=' <==> ')
			print(node.data, '| ', 'prev:', prev_data, '| next:', nextn_data)
			if node.nextn == None:
				break
			node = node.nextn
		print('NULL')

	def showNodes(self):
		# shows node datapoints in adjacence to eachother
		node = self.head
		while node is not None:
			print(node.data, end=' <==> ')
			node = node.nextn
		print('NULL')

	def peekHead(self):
		print (self.head.data)

	def peekTail(self):
		print(self.tail.data)

	def insertNode(self,data, position):
		# Position is index in which to insert node
		if type(data) != str:
			print('Only string values accepted.')
			return
		if position >= len(self.list):
			print('Index out of range')
			return

		if position == 0:
			# if new head has to be created
			new_node = Node(data=data, nextn=self.head, prev=None)
			nextn = new_node.nextn
			nextn.prev = new_node
			self.head = new_node
		elif position == -1:
			# if new tail has to be created
			new_node = Node(data, prev=self.tail, nextn=None)
			self.tail.nextn = new_node
			self.tail = new_node
		else:
			targ_node = self.list[position] # rightward shift
			prev_node = targ_node.prev # leftward shift

			# create node with accurate pointers
			new_node = Node(data, prev=targ_node.prev, nextn=targ_node)
			# change left node to point nextn to new node
			prev_node.nextn = new_node
			# change right node to point prev to new node
			targ_node.prev = new_node

	def removeNode(self, data):

		node = self.head

		# if head needs to be changed
		if node.data == data:
			self.head = node.nextn
			node.nextn.prev = None
			self.list.remove(node)
			return


		while node is not None:
			if node.data == data:
				break
			node = node.nextn
			if node == None:
				# If nextn == none then we have arrived at the end of the list,
				# therefore the node does not exist.
				print(f'Node with value "{data}"  not found')
				return

		# if tail is removed
		if node.nextn == None:
			self.tail = node.prev
			self.tail.nextn = None
			self.list.remove(node)
			return
		elif node.nextn != None and node.prev != None:
			# If the nodes are not a head or tail
			nextn = node.nextn
			prev = node.prev
			nextn.prev = prev
			prev.nextn = nextn
			self.list.remove(node)

		

data = ['rishi', 'abhishek', 'aman', 'ahan', 'yohu', 'sid']
new_list = DLinkedList().
new_list.initializeList(data)




	








		









