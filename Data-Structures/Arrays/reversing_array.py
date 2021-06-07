def reverse_array(arr):
    start = 0
    end = len(arr)-1
    while start < end:
        arr[start],arr[end] = arr[end],arr[start]
        start = start +1
        end = end - 1
    return arr

arr1 = [1,2,3,4]
print (reverse_array(arr1))
