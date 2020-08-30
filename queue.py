"""
Queues

A Queue is a data structure where data is arranged in a queue, and follows 
FIFO - First in First out - methodology to Add and Remove data.

To add data, it is placed in the back of the queue, and to remove data,
the last value will be removed. 

Applications of Queues:
- Waiting line models require queues, such as scheduling Process execution in an operating system, queues
at movie theatres, etc.
- Web servers servicing reqeusts using a FIFO algorithm.
- Breadth first traveral of a graph. (Network)

Adding and Removal in queues can be implemented in a range of ways, from a priority based algorithm,
to the "smallest/shortest" element first model.

Time Complexity:

Enqueue: O(1)
Dequee: O(1)
Peeking: O(1)
Contains: O(n)
Removal at index: O(n)
IsEmpty: O(1)
"""

class Queue:
	"""
	This Queue is a left to right queue, where the start of the queue
	is at index 0 and the end is index -1 (the last element).

	Newly added elements will be inserted at the end of the queue.
	Items to be dequed/removed will be those at the start of the queue at index 0.
	"""
	def __init__(self):
		self.queue = []

	def peek(self):
		if len(self.queue) > 0:
			return self.queue[0]
		else:
			print("Queue is Empty.")
	def enqueue(self, data):
		self.queue.append(data)
		return True

	def dequeue(self):
		if len(self.queue) > 0:
			del(self.queue[0])
			return True
		else:
			print("Queue is Empty.")

	def showQueue(self):
		if len(self.queue) > 0:
			print(self.queue)
		else:
			print("Queue is Empty.")

	def size(self):
		return len(self.queue)







