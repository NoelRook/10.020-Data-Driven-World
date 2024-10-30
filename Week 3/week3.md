Week 3: Recursion, Merge Sort
Divide and conquer
________________________________________________________________

__Creating a recursive function__
1. Base case: when does the function stop running?
2. Recursive case: How does solving 1 problem cascade into solving many problems

__Factorial problem/function__
input: n, number to factorise
output: resulting number

steps:
1. if n <= 1:
    1.1. return 1 [base_case]
2. Else:
    2.1. return n * factorial(n-1) [recursive_case]

__Tower of Hanoi__
rules: Bigger disk cannot be placed on top of smaller disk, only 1 disk can be moved at a time

notes: Think about moving 2 disks from tower A to tower C with

A: Source, B: auxiliary , C: Destination

solution: [Move A to B, Move A to C, Move B to C]

Therefore,
input: N, source, destination, auxiliary 

Steps:
Tower_of_Hanoi(n, source, destination, auxiliary):
    1. if n is 1 disk: [base_case]
        1.1. Move disk from source to destination
    2. else: [recursive_case]
        2.1. Move n-1 disk from source to auxiliary tower
        2.2. Move last disk from source to destination tower
        2.3. Move first n-1 disk from auxiliary to destination tower

computational time: O(N)




__MergeSort__
tl;dr steps:
1. split the array into 2 smaller arrays
2. sort the smaller array from smallest to largest
2. created a sorted array to store the sorted values
3. starting from the first number in each array, compare the numbers in each array with each other
    3.1. place the smaller number from each comparison until you have a sorted array

__1.Mergesort(array, p, r):__
input: unsorted array, p = index of the beginning of the array, r = index of the end of the array
output: None, sorted in place

Steps:
1. if r-p>0:  # if end index - start index > 0
    1.1. calculate q = (p+r)/2 # get the middle of the index
    1.2. call mergesort(array, p, q) # create an array containing the 
    1.3. call mergesort(array, p+1, r)
    1.4. call Merge(array, p, q, r)



__2. Merge(array, p, q, r):__
input: array, p: beginning index of array, q: ending index of left array, r: ending index of right array
output: None, sort in place

Steps:
(setup)
1. nleft = q - p + 1 #length of left array
2. nRight = r - q #length of right array 
3. left_array = array[p:q]
4. right_array = array[q+1:r]
5. left = 0 
6. right = 0  
7. dest = p # initialse the dest arrow, starting from p in the sorted arrays

(merging step)
8. while (left < nleft) and (right < nright):  #in the case where both left and right arrays have elements to compare
    8.1. if left_array[left] < right_array[right]: # if the value of left array is less than value of right array
        8.1.1. array[dest] = left_array[left] # take the array as the sorted array
        8.1.2. left = left+1 # move the left array pointer up
    8.2. else:
        8.2.1. array[dest] = right_array[right]
        8.2.2. right = right +1 # move the right array pointer up
    8.3. dest = dest+1 # move the dest pointer up by 1
 
9. while (left < nleft): # in the case where only left array has integers in it
    9.1. array[dest] = left_array[left]
    9.2. left = left +1
    9.3. dest = dest +1

10. while (right< nright): # in the case where only right array has integers in it 
    10.1. array[dest] = right_array[right]
    10.2. right = right + 1 
    10.3. dest = dest + 1



