def selection_sort(arr):
    for min_index in range(len(arr)):
        minimum = min_index
        for j in range(min_index+1,len(arr)):
            if arr[minimum] > arr[j]:
                minimum = j
        arr[minimum],arr[min_index] = arr[min_index],arr[minimum]
    
    return arr

arr = [1000,323,89,10,-99232,40309,893,-219,908,7]
print(selection_sort(arr))