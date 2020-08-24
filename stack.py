"""
A stack data structure is similar to any general stack, where items are place on top of eachother.
This data structure stores data elements in a similar way where data is stored on top of eachtoher. 

Items can only be added and removed from one end of the stack - the top.
Hence, it follows a Last in First out (LIFO) ordering in respect to insertion and removals.

The other end of the stack is known as the base.

Methods commonly known as PUSH (add) and POP (remove) are common operations to handle adding
and removing.

Applications of a Stack:

- Undo mechanism in text editors
- Back tracking in a  maze (retracing steps)
- Conduct a Depth First Seatch on a graph
- Used in compiler syntax for brackets and curly braces

Time Complexity of operations:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Search: O(n)
- Size O(1)


"""


class Stack:

"""
A basic stack class with typical methods that come with this data structure.
"""

	def __init__(self):
		self.stack = []


	def add(self, data):
		# Append adds data to the "top-end" of the stack
		self.stack.append(data)
		print('Successfully added item.')
		return 

	def remove(self):
		# If the stack is empty it will throw and error
		if len(self.stack) > 0: 
			self.stack.pop()
			print('Successfully removed item.')
			return
		else:
			print('Stack is empty.')
			return

	def showStack(self):
		print(self.stack)
		return

	def size(self):
		print(len(self.stack))

	def is_empty(self):
		if len(self.stack) > 0:
			return False
		else:
			return True
	def peek(self):
		return self.stack[-1]


