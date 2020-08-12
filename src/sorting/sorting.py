
def merge(arrA, arrB):
    elements = len(arrA) + len(arrB)
    merged_arr = [0] * elements

    for i in range(elements):
        if not arrA:
            for index in range(len(arrB)):
                merged_arr[i] = arrB[index]
                i += 1
            break
        if not arrB:
            for index in range(len(arrA)):
                merged_arr[i] = arrA[index]
                i += 1
            break
        if arrA[0] <= arrB[0]:
            merged_arr[i] = arrA.pop(0)
        else:
            merged_arr[i] = arrB.pop(0)
    
    return merged_arr


def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    h = len(arr)//2
    arrA = merge_sort(arr[:h])
    arrB = merge_sort(arr[h:])
    arr = merge(arrA, arrB)
    return arr

# STRETCH: implement the recursive logic for merge sort in a way that doesn't 
# utilize any extra memory
# In other words, your implementation should not allocate any additional lists 
# or data structures; it can only re-use the memory it was given as input
def merge_in_place(arr, start, mid, end):
    pass


def merge_sort_in_place(arr, l, r):
   pass

