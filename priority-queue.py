"""
A priority Queue is an implementation of the queue data structure, 
where the removal/deqeuing of an item depends on its priority value.

If an element has a high priority, it is likely to be moved out of the queue 
before an element with lower priority.

Priority is usually assigned using an integer, with the direction of magnitude 
varying with the priority range. I.e. The priority magnitude can be increasing in descending order
with 1 being the highest. On the flip side, priority can be increasing in ascending order 
with 1 being the lowest.


Applications:
- Used in certain implementations of Djikstras Shortest Path Algorithm
- Anytime the next 'best' or 'worst' item in the queue needs to be dynamically fetched.
- Used in Huffman coding (for lossless data compression)
- Best first sestch algorithms such as A* 
- Minimum spanning tree (MST) algorithms

Time Complexity:
- Binary Heap construction: O(n)
- Polling/Dequing(O(log(n)))
- Peeking: O(1)
- Adding: O(log(n))
- Removal: O(n) but can be reduced to O(log(n)) with hash tables
"""


class BinaryMinHeap:
	"""
	A Binary tree heap is used commonly in the application of a priority Queue,
	an abstract data type (ADT). 

	There are two types of Binary Heaps:
	Min Heap: the root is smaller than its children and leaf nodes
	Max Heap: The root is larger than its children and leaf nodes

	In some cases the child can be equal to the parent.

	A complete Binary Tree Heap is a tree in which every level, except the last, is completely
	filled and all the nodes are as far left as possible.

	Binary Heaps can be represented using arrays/lists.

	Assuming all the contraints of binary heap invariant have been met:
	If i is the index of the parent node:
		-  To access the left child of a node, it will be found at index 2i + 1
		-  To access the right child of a node, it will be found at index 2i + 2


	"""

	def __init__(self):
		self.heap = []
		self.type = ''

	def initialiseHeap(self, nodes):
		# Check if the data is sorted in ascending or descending order
		# It will only accept integers.
		if nodes[0] < nodes[-1]:
			self.heap = nodes
		else:
			print('Data not formatted correctly.')


	def size(self):
		return len(self.heap)


		"""
		The method below - insert() -  inserts data at the last index of the list, or the left-most position 
		available in the tree, which is always going to be at the lowest level. 

		If it is a min heap, the node will switch positions with its parent until the Heap invariant is satisfied, in this case 
		until it is in a position where it is smaller than its children, the node will keep switching
		positions. This methods is known as "bubbling up", "percolating up", "swimming up", etc. 

		The opposite applies in a max heap where the new node will bubble up until it is larger than its parent
		nodes. 
		"""
	def insert(self, data):
		if self.size() > 0:
			self.heap.append(data)
			self.percolate_up(-1)

		

		"""
		The method below -  poll() - is used to remove the root value of the tree as it is likeliest to be the point
		of highest interest. 

		The root is swapped with the right most node of the last level,
		which is the last index (-1) in the array/list representation. After
		swapping, the old root node is removed.

		Then, the new root bubbles down until the heap invariant is satisfied of either being a min or max heap. 
		The child where the difference is greatest is the node with which the target node swaps places with.

		If the children nodes have the same value, swap with the left node. 
		"""
	def poll(self):
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		self.heap.pop()
		self.percolate_down(0)


		"""
		The method below - removaAt() - is exactly like polling, where the target node swaps positions with the last node in the tree,
		and is removed. Then node swapped into the target nodes position either bubbles up or down depending
		on the tree variation.

		With this method always ensure if the heap invariant is satisfied before swapping.

		"""
	def removeEl(self, data):
		pos = ''
		for el in self.heap:
			if el == data:
				pos = self.heap.index(el)

		if pos == '':
			print('This element does not exist')
			return 0
		self.heap[pos], self.heap[-1] = self.heap[-1], self.heap[pos]

		self.heap.pop()
		if len(self.heap) >= 2:
			# Check if child node is smaller
			if self.heap[pos] > self.heap[pos // 2]:
			# if the current element at index pos is larger then 
			# if the  
				self.percolate_down(pos)
			# check if child node is smaller
			elif self.heap[(2 * pos) + 1] < self.heap[pos]:
				self.percolate_up(pos)
		



	def percolate_up(self, position):
		if position == -1:
			position = len(self.heap) - 1
		while position // 2 >= 0:
			if self.heap[position] > self.heap[position // 2]:
				break

			if self.heap[position] < self.heap[position // 2]:
				self.heap[position // 2], self.heap[position]= \
				self.heap[position], self.heap[position // 2]
			position = position // 2
	
	def percolate_down(self, position):
		# highest possible index value
		heap_capacity = len(self.heap) -1
		heap = self.heap
		while position < heap_capacity + 1 and position is not None:
			# index value of left and right children
			if position == None:
				break
			left = (2*position) + 1
			right = (2*position) + 2

			if left > heap_capacity:
				# Given the nature of binary trees
				# if there is no left child node of the current node
				# it can be assumed that there are no further children.
				break
			# follow down the branch where the difference is greater between the current
			# value and children
			mc = self.min(left, right, position) # mc = min child (smaller value)
			heap[mc], heap[position] = heap[position], heap[mc]
			position = mc



	def min(self, left, right, pos):
		heap = self.heap 
		if left == None:
			return right
		elif right == None:
			return left
		l = heap[pos] - heap[left]	
		r = heap[pos] - heap[right]
		if r > l:
			return right
		else:
			return left
	def displayTree(self):
		heap = self.heap
		spaces = len(heap)//2
		# original right most node
		bingo = 2 
		for el in heap:
			if heap.index(el) == 0:
				print('	' * (spaces), el)
				spaces = 0.75 * float(spaces)
				# continue
			else:
				
				print('	' * (int(spaces)), el,end='')
				if heap.index(el) == bingo:
					print('\n')
					# according to the structure of a binary tree
					# the last node of a level is i*2 + 2 (think right node formula)
					# starting with 2, the next right most node is i = 6, then i = 14 and so on.
					bingo = int(heap.index(el)*2 + 2) 
					spaces = 0.75 * float(spaces)
		print('\n' * 3)






data = [0,1,2,4,5, 6, 7, 8, 12, 14, 18, 20, 27, 30]
heap_tree = BinaryMinHeap()
heap_tree.initialiseHeap(data)

heap_tree.insert(3)
# print('Original: ',heap_tree.heap)
# heap_tree.displayTree()
# print('finished: ',heap_tree.heap)
heap_tree.displayTree()


