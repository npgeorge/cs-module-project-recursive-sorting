# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements # what does this do for us?
    # base case is when the number of elements = number of merged
    # this is always true
    #if elements == merged_arr:
    #    return

    #merge two sorted lists
    #print("Elements: ", elements)
    #print("Merged List: ", merged_arr)
    #print(arrA + arrB)

    # split list a into elements only
    if arrA and arrB:
        if arrA[0] > arrB[0]:
            arrA, arrB = arrB, arrA
        return [arrA[0]] + merge(arrA[1:], arrB)

    return arrA + arrB

arrA = [0,1,2,3]
arrB = [4,5,6,7]

print(merge(arrA, arrB))

# TO-DO: implement the Merge Sort function below recursively
def merge_sort(arr):
    # if list is greater than 1
    if len(arr) > 1:
        #find mid
        mid = len(arr) // 2
        #left
        left = arr[:mid]
        #right
        right = arr[mid:]

        #sort left recursively
        left = merge_sort(left)
        #sort right recursively
        right = merge_sort(right)

        #create an empty list
        arr = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                arr.append(left[0])
                left.pop(0)
            else:
                arr.append(right[0])
                right.pop(0)
        
        for i in left:
            arr.append(i)
        for i in right:
            arr.append(i)

    return arr

# Input list 
a = [12, 11, 13, 5, 6, 7] 
print("Given array is") 
print(*a) 
  
a = merge_sort(a) 
  
# Print output 
print("Sorted array is : ") 
print(*a) 

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    # Your code here
    pass


def merge_sort_in_place(arr, l, r):
    # Your code here
    pass

