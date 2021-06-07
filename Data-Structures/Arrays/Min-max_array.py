#Min-Max elements from given array using minimum no. of comaparisons
def getminmax(low,high,arr):
    if low == high: #if single element is present
        arr_max = arr[low]
        arr_min = arr[low]
        return (arr_min,arr_max)

    elif high == low+1: #if two elements are present
        if arr[low]>arr[high]:
            arr_min = arr[high]
            arr_max = arr[low]
        else:
            arr_min = arr[low]
            arr_max = arr[high]
        return (arr_min,arr_max)

    else: #more than 2 elements
        mid = int((low+high)/2)
        arr_min1,arr_max1 = getminmax(low,mid,arr)
        arr_min2,arr_max2 = getminmax(mid+1,high,arr)
    return (min(arr_min1,arr_min2),max(arr_max1,arr_max2))

arr = [12,34,54,28,62]
print (getminmax(0,len(arr)-1,arr))

