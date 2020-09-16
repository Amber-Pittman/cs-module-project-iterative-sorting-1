# TO-DO: Complete the selection_sort() function below
def selection_sort(arr):
    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        current_index = i
        smallest_index = current_index
        # TO-DO: find next smallest element
        # (hint, can do in 3 loc)
        # Your code here
        for x in range(current_index + 1, len(arr)): # move an item to the right
            if arr[x] < arr[smallest_index]: # if right value smaller, make it the minimum value
                smallest_index = x

        # TO-DO: swap
        # Your code here
        arr[smallest_index], arr[current_index] = arr[current_index], arr[smallest_index]
    return arr


# TO-DO:  implement the Bubble Sort function below
def bubble_sort(arr):
    # Your code here
    index_len = len(arr) - 1 # can't compare last element since there aren't any numbers after it
    sorted = False # breaks out of loop when needed

    while not sorted:
        sorted = True
        for x in range(0, index_len): 
            if arr[x] > arr[x + 1]: # left value greater than right value, it's not sorted
                sorted = False
                arr[x], arr[x + 1] = arr[x + 1], arr[x] # swap them to sort
    return arr

'''
STRETCH: implement the Counting Sort function below

Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).

Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 

What is the time and space complexity of the counting sort algorithm?
'''
# def counting_sort(arr, maximum=None):
#     # Your code here


#     return arr
