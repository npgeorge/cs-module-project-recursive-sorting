# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    if start <= end:
        mid = (start + end) // 2
        
        print("Searching list...")
        print("start", start)
        print("mid", mid)
        print("end", end)
        print("Middle index value of list: ", arr[mid])
        
        # return True if we find our target
        if arr[mid] == target:
            #return arr[target]
            print("list: ", *arr)
            return len(arr)

        if arr[mid] < target:
            print("Split towards end...")
            print("list: ", arr[])
            return binary_search(arr, target, mid + 1, end)
        elif arr[mid] > target:
            print("Split towards start...")
            print("list: ", arr[:mid])
            return binary_search(arr, target, start, mid - 1)
    
    return False

#arr = [-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9]
#target = 5
#start = 0
#end = len(arr) - 1

#print(binary_search(arr, target, start, end))

#def contains(elements, value, left, right):
#    if left <= right:
#        middle = (left + right) // 2
#
#        if elements[middle] == value:
#            return True
#
#        if elements[middle] < value:
#            return contains(elements, value, middle + 1, right)
#        elif elements[middle] > value:
#            return contains(elements, value, left, middle - 1)
#
#    return False


# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
def agnostic_binary_search(arr, target):
    # Your code here
    return