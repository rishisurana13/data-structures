"""
A priority Queue is an implementation of the queue data structure, 
where the removal/deqeuing of an item depends on its priority value.

If an element has a high priority, it is likely to be moved out of the queue 
before an element of a lower priority.

It is most optimally implemented using the Binary Heap of the heap invariant.

There are two types of Binary Heaps:
Min Heap: the root is smaller than its children and leaf nodes
Max Heap: The root is larger than its children and leaf nodes

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
"""