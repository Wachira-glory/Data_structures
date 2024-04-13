# Heaps
A heap is a complete binary  tree-based data structure that satisfies the heap property, where the root node is always largest or smallest among all the other nodes depending on the heap type.
There are two types of heaps:max-heap and min-heap
Max-heap: The key at the root node of a Max-Heap must be greater than or equal to the key at each of its offspring.
Min-heap: The key at the root node of a Min-Heap must be less than or equal to the key at each of its offspring.

The common operations inlude:
Insert: This is the adding a value to a heap
Extracting: This is getting an element in a heap, which can be either the maximum element or a minimum element based on the heap type
heapify: This is the process of creating a heap

APPLICATIONS OF HEAP DATA STRUCTURE
The heap data structure is frequently used to create priority queues where elements are kept in a heap and arranged according to their priority.

Algorithms for job scheduling use the heap data structure to arrange tasks according to their deadlines or priorities. The heap data structure is a helpful data structure for work scheduling applications because it provides quick access to the task with the highest priority.

ADVANTAGES OF HEAPS

Efficient insertion and deletion of elements is possible using the heap data structure. When a new element is introduced to the heap, the heapify action is used to move it up to the proper location from the bottom of the heap. Similar to this, the heap is reorganized using the heapify method when an element is removed from it; in this case, the bottom element takes its place.

Implementing a priority queue with the highest priority element always at the head of the heap is a typical use for the heap data structure. The heap is a useful data structure for building priority queues because it provides constant-time access to the element with the highest priority.

DISADVANTAGES OF HEAPS
Because the heap data structure is meant to preserve a particular elemental order, it is not very flexible. This implies that some applications that call for more flexible data structures might find it unsuitable.
# Heaps
