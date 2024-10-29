Week 2 notes: Binary heaps, Heapsort
___________________________________________________

Binary Heaps
- Tree with leaf structure

# returning the parent of the child node
Parent_of(index):
    1. return index-1/2

# returns the left child
Left_of(index):
    1. return index*2 + 1

# Returns the right child
Right_of(index)
    1. return index*2 + 2

# returns index of the max_child of a parent node
Max_child(array, index, heap_size):
    1. if Right_of(index) > heap_size:
        1.1. Return Left_of(index)
    2. else:
        2.1 if array[left_of(index)]> array[right_of(index)]:
            2.1.1. Return left_of(index)
        2.2. Else:
            2.2.1 Return Right_of(index)

# create a max_heap a node and all of its subsequent children
max_heapify(array, index, heap_size):
    1. current_i = index
    2. swapped = True
    3. while left_of(current_i)< heap_size and swapped ==True:
        3.1. swapped = False
        3.2. max_child_i = Max_child(array, current_i, heap_size)
        3.3. If array[max_child_i] > array[current_i]:
            3.3.1. swap(array[max_child_i], array[current_i])
            3.3.2. swapped = True
        3.4. current_i = max_child_i

# create a max heap out of the array built
build_max_heap(array):
    1. n = len(array)
    2. starting_idx = (n//2) -1
    3. for current_idx in range(starting_idx,-1,-1)
        3.1. max_heapify(array, current_idx, size)

# sort the heap in ascending order
heapsort(array):
    1. build_max_heap(array)
    2. heap_end_pos = len(array) - 1  # index of the last element in the heap
    3. while heap_end_pos >0 :
        3.1. swap(array[0], arary[heap_end_pos])
        3.2. build_max_heap(array, 0, heap_end_pos) #update the heap_end_pos to reflect the unsorted array
        3.3. heap_end_pos -= 1
