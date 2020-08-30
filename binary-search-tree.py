"""

**Tree** 
A Tree is an undirected graph with the following definitions:
- An Acyclic connected graph
- A connected graph with N nodes and N-1 edges
- A Graph in which any two vertices are connected by exactly one path

The parent of a root node is always itself. 

Terminology:

Child Nodes:
Nodes in a tree that extend from another node are known as child or children nodes. 

Parent Nodes:
The node from which a child node extends is a parent nodes.

Leaf Nodes:
A leaf node is a node that has no children.

Sub Tree:
A tree entirely contained within another. 
A subtree can consist of a single node.

"""

class Node:
	def __init__(self, left, right, parent, data):
		self.data = data
		self.left = left
		self.right = right
		self.parent = parent


class BinarySearchTree:
	"""

** Binary Tree **

A binary Tree is a tree for which every node has two child nodes.
It satisfies the BST invariant: The left subtree has smaller elements and the right subtree 
has larger elements. Where the left child is smaller its parent and the right child
is larger then its parent.

Binary search trees are not limited to only numbers. Any data that can be ordered and compared can be 
placed inside a BST.

Time Complexity:

Insert: O(log(n))
Delete: O(log(n))
Remove: O(log(n))
Search: O(log(n))

All the above operations have a worst case time complexity of O(n)

Applications:
- Huffman coding algorithm
- Reduced search time for data that is sorted
	"""

	def __init__(self):
		self.root = None
		self.count = 0

	def insert(self, data):
		"""
		When inserting an element, the tree must be traversed to decide an 
		optimal position to insert at to maintain the BST invariant. 

		The following decisions must be made while iterating over the tree:
		- Recurse/traverse down the left subtree/child
		- Recurse/traverse down the right subtree/child
		- Handling a duplicate value
		- Creating a new node

		"""
		# Iterations always start from the root note
		
		traversing = True
		curr_node = self.root
		next_node = None

		if self.count == 0:
			new_node = Node(data=data, left=None,right=None, parent=None)
			self.root = new_node
			self.count += 1
		else:
			new_node = Node(data=data, left=None, right=None, parent=None)
			self.count += 1
			
			while traversing:
				# go left
				if new_node.data < curr_node.data:
					next_node = curr_node.left
					if next_node == None:
						curr_node.left = new_node
						new_node.parent = curr_node
						break
				# go right
				elif new_node.data > curr_node.data:
					next_node = curr_node.right
					if next_node == None:
						curr_node.right = new_node
						new_node.parent = curr_node
						break
				# Duplicate value handler
				elif new_node.data == curr_node.data:
					del new_node
					print("duplicates not allowed.")
					break

				curr_node = next_node
		
			

	def remove(self, el):
		"""
		Steps to remove a node from a bst:
		1) Find the element
		2) Replace the node with a successor, if any.

		There are four cases to handle in removing a node:
		1) The node to be removed is a leaf node.
		2) The node to be removed has a right subtree but no left subtree.
		3) The node to be removed has a left subtree but no right subtree.
		4) The node to be removed has a right and left subtree.

		Case 1: Leaf node
		It can be removed without any side effects

		Case 2 and 3:
		The successor of the node to be removed will the root node of the subtree which
		is also the child node of the node being removed.

		Case 4:
		The successor can be either the largest value in the left subtree or the
		smallest value in the right subtree.

		"""
		targ_node = self.find(el)
		if targ_node == None:
			return
		parent_node = targ_node.parent

		# Case 1: Leaf node
		if targ_node.left == None and targ_node.right == None:

			# determine if the node is a left or right child node
			# Left child
			if parent_node.data > targ_node.data:
				del targ_node
				parent_node.left = None
				# self.count -= 1
				return

			# Right child
			elif parent_node.data < targ_node.data:
				parent_node.right = None
				del targ_node
				self.count -= 1
				return

		# Case 2: Only has left subtree
		elif targ_node.right == None and targ_node.left != None:
			# Assign parent to left subtree root
			targ_node.parent.left = targ_node.left
			targ_node.left.parent = parent_node
			del targ_node
			self.count -= 1
			print("successfully deleted node.")
			return

		# Case 3: Only has right subtree 
		elif targ_node.left == None and targ_node.right != None:
			print('case 3')
			targ_node.parent.right = targ_node.right
			targ_node.right.parent = parent_node
			del targ_node
			self.count -= 1
			print("successfully deleted node.")
			return

		# Case 4: Has left and right subtrees
		elif targ_node.left != None and targ_node.right != None:
			"""
			Find either the largest value in the left subtree
			or the smallest value in the right subtree
			"""
			# from the left node dig as far right as possible
			successor = self.dig_right(targ_node.left)

			# extract value of successor
			val = successor.data
			# Recurse and remove sucessor node
			self.remove(successor.data)
			# assign successor value to target node
			targ_node.data = val
			self.count -= 1
			print("successfully deleted node.")




	def dig_right(self, node):
		# Goes as far right as possible from the given starting point
		"""
		This function and dig_left() perform the same task, of digging as far right/left 
		as possible.

		These functions can be used to:
		- Find a sucessor node
		- traverse to one end of the tree in one direction
		- Help determine if a tree is left or right heavy

		"""
		curr_node = node
		traversing = True
		while traversing:
			next_node = curr_node.right
			if next_node == None:
				return curr_node
			curr_node = next_node

	def dig_left(self, node):
		curr_node = node
		traversing = True
		while traversing:
			next_node = curr_node.left
			if next_node == None:
				return curr_node
			curr_node = next_node

			



	def find(self,el):
		"""
		When finding a node, the traversal path is the same when inserting it, where the following
		decisions must be made:
		- Recurse/traverse down the left subtree/child
		- Recurse/traverse down the right subtree/child
		- Handling a duplicate value
		- If the next node(s) are null then the element does not exist

		This function returns the index value of the node if it exists, or None/null
		if it does not exist.
		"""
		curr_node = self.root
		traversing = True
		while traversing:
			if curr_node.data == el:
				# print(curr_node.data)
				return curr_node

			if el < curr_node.data:
				# go left
				curr_node = curr_node.left
			elif el > curr_node.data:
				# go right
				curr_node = curr_node.right

			if curr_node == None:
				print('Node does not exist.')
				return curr_node


	def showTree(self, node):
		# Recursive function to show all nodes and child nodes
		# always equate node input param to self.root when
		# calling function at first
		# Shows in order or parent, left and right child
		# if there is no left/right child then None will be displayed
		# its shows the left child of the root's subtree in entirety and then the right subtree's nodes. 

		node_left = node.left
		node_right = node.right

		if node_left == None and node_right != None:
			node_left = None
		elif node_right == None and node_left != None:
			node_right = None
		
		if node_left != None and node_right != None:
			print(node.data,node_left.data, node_right.data)
			return self.showTree(node_left), self.showTree(node_right)
		elif node_right != None and node_left == None:
			print(node.data, node_left, node_right.data)
			return self.showTree(node_right)
		elif node_left != None and node_right == None:
			print(node.data, node_left.data, node_right)
			return self.showTree(node_left)
		else: 
			return

	def treeHeight(self):
		left_depth = 0
		right_depth = 0
		node = self.root
		left_node = node.left
		right_node = node.right
		while True:
			
			if left_node != None:
				left_depth += 1
				left_node = left_node.left
			
			if right_node != None:
				right_depth += 1
				right_node = right_node.right
			
			if left_node == None and right_node == None:
				break
			
		
		print(f'Left Depth: {left_depth}  \nRight Depth: {right_depth}')
		return left_depth, right_depth

	def inorder(self, node):
		# Traverse left subtree, print the value of the node, the traverse the right subtree
		if node == None:
			return
		self.inorder(node.left)
		print(node.data)
		self.inorder(node.right)

	def preorder(self, node):
		# Print value of the current node then traverse the left subtree
		# followed by the right subtree
		if node == None:
			return
		print(node.data)
		self.preorder(node.left)
		self.preorder(node.right)

	def postorder(self, node):
		# Traverse the left subtree followed by the right subtree
		if node == None:
			return
		self.postorder(node.left)
		self.postorder(node.right)
		print(node.data)

	def bfs(self, node):
		# Breadth first search
		queue = [node]
		bfs = []
		curr_node = node
		while True:
			if curr_node.left != None:
				queue.append(curr_node.left)

			if curr_node.right != None:
				queue.append(curr_node.right)
			
			bfs.append(curr_node.data)

			del(queue[0])
			if len(queue) == 0:
				break
			curr_node = queue[0]
		print(bfs)








bst = BinarySearchTree()
bst.insert(11)
bst.insert(6)
bst.insert(15)
bst.insert(3)
bst.insert(8)
bst.insert(1)
bst.insert(5)
bst.insert(13)
bst.insert(17)
bst.insert(12)
bst.insert(14)
bst.insert(19)
# bst.showTree(bst.root)

bst.bfs(bst.root)

















