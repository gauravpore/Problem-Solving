#kth largest and smallest element in an array
def kth_largest(k,arr):
    arr.sort()
    arr.reverse()
    return arr[k-1]

def kth_smallest(k,arr):
    arr.sort()
    element = arr[k-1]
    return element


arr1 = [5,3,8,9,11]
print (kth_smallest(2,arr1))
print (kth_largest(3,arr1))