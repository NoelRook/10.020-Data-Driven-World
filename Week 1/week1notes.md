Week 1 notes

objective: Check Palindrome
input: string
output: bool
function:
1. for every idx in string len//2 
    1.1. if string[idx] != string[len(s)-idx-1]
    1.1.1 return False
2. return True
____________________________________________________________________________

Bubble sorts ->
input: unsorted array
output: None, sorted in place

V1 (O(n^2)): 
Steps:
1. n = length of array
2. for outer_index from 1 to n-1:
    2.1. for inner_index from 1 to n - 1:
        2.1.1. if array[inner_index-1] > array[inner_index]:
        2.1.1.1 swap(first_number, second_number)

V2 (O(n^2)): 
steps:
1. initiate n as len of array
2. initiate swapped == True
3. while swapped == True:
    3.1. set swapped = False
    3.2. for idx in range(0, n-1):
        3.2.2. if array[idx] > array[idx+1]
            3.2.2.1. swap positions
            3.2.2.2. set swapped = True
4. return count

V3 (n^2):
steps:
1. n = length of array
2. swapped = True
3. while swapped == True:
    3.1. swapped = False
    3.2. For inner_idx from 1 to n-1:
        3.2.1. if array[inner_idx-1]> array[inner_idx]:
            3.2.1.1. swap(array[inner_idx-1], array[inner_idx])
            3.2.1.2. swapped = True
    3.3. n = n-1

V4 (O(n^2)):
steps:
1. n = length pf array
2. swapped = True
3. while swapped == True:
    3.1. swapped = False
    3.2. new_n = 0
    3.3. For inner_index from 1 to n-1:
        3.3.1. if array[inner_index-1] > array[inner_index]:
            3.3.1.1. swap(array[inner_index-1] , array[inner_index])
            3.3.1.2. swapped = True
            3.3.1.3. new_n = inner_index 
    3.4. n = new_n

Optimised Bubblesort (O(n^2))
steps:
1. for i in range(len(array)):
    1.1. for j in range(len(array)-i-1):
        1.1.1. if array[j] > array[j+1]:
            1.1.1.1. swap(array[j], array[j+1])

____________________________________________________________________________
Insertion sort
Input: unsorted array
output: None, sort in place

V1 (O(n^2))
steps:
1. n = len of array
2. For outer_idx in range(1 to n-1): # cycle throught all the elements in the list
    2.1. inner_idx = outer_idx  # set the current index as the main char
    2.2. while inner_idx>0 AND array[inner_idx] < array[inner_idx-1]: # while the inner_idx is still in the list and next number 
        2.2.1. swap (array[inner_idx], array[inner_idx-1])
        2.2.2 inner_idx = inner_idx-1

V2
steps:
1. n = len of array
2. For outer_idx in range(1 to n-1):
    2.1. inner_idx = outer_idx
    2.2. temporary = array[inner_idx]
    2.3. while inner_idx>0 and temporary < array[inner_idx-1]: 
        2.3.1. array[inner_idx]= array[inner_idx-1] # move the bigger element to the right
        2.3.2. inner_idx = inner_index-1 # new inner index is chosen to the left of the current index to be compared
    2.4. array[inner_idx] = temporary #save the temporary number into its final destination





