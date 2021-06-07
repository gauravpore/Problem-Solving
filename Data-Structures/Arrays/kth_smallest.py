

def partition(arr,l,r):
    pivot = arr[r] #last index
    cur = l #0th index
    for i in range(l,r):
        if arr[i]<pivot:
            arr[cur],arr[i]=arr[i],arr[cur]
            cur+=1
    arr[cur],arr[r] = arr[r],arr[cur]
    return cur

def kthsmallest(arr,l,r,k):
    if (k>0 and k<=len(arr)):
        index = partition(arr,l,r)
        if index == k-1:
            return arr[index]
        if index>k-1:
            return kthsmallest(arr,l,index-1,k)
        if index<k-1:
            return kthsmallest(arr,index+1,r,k)
    return     


arr = [10, 4, 5, 8, 6, 11, 26]
n = len(arr)
k = 7
print("K-th smallest element is ", end="")
print(kthsmallest(arr, 0, n - 1, k))

