def linear_search(arr, target):
    # Your code here
    for x in range(0, len(arr)):
        if arr[x] == target:
            return x

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    # set up pointers
    start = 0
    end = len(arr) - 1

    found = False # break out the loop when needed

    # if the midpoint hasn't been found between the first index and the last check if the target is the same as the midpoint already
    while start <= end and not found: 
        middle = (start + end) // 2

        if arr[middle] == target: # if target is already found and is the same as the middle, return the middle of the list
            return middle
        else: # otherwise, divide the list in half
            if target < arr[middle]:
                end = middle - 1
            if target > arr[middle]:
                start = middle + 1
    return -1  # not found
