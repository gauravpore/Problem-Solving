

def partition(arr,l,r):
    pivot = arr[r] #last index
    cur = l #0th index
    for i in range(l,r):
        if arr[i]<pivot:
            arr[cur],arr[i]=arr[i],arr[cur]
            cur+=1
    arr[cur],arr[r] = arr[r],arr[cur]
    return cur

def kthlargest(arr,l,r,k):
    if (k>0 and k<=len(arr)):
        index = partition(arr,l,r)
        if index == len(arr)-k:
            return arr[index]
        if index>len(arr)-k:
            return kthlargest(arr,l,index-1,k)
        if index<len(arr)-k:
            return kthlargest(arr,index+1,r,k)
    return


arr = [10, 4, 5, 8, 6, 11, 26]
n = len(arr)
k = 3
print("K-th largest element is ", end="")
print(kthlargest(arr, 0, n - 1, k))

