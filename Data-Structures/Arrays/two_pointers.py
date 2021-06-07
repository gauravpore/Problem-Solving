

def twoPairSum(arr,s):
    low = 0
    high = len(arr)-1
    while low<high:
        if arr[low]+arr[high]==s:
            return arr[low],arr[high]
        elif arr[low]+arr[high]>s:
            high-=1
        else:
            low+=1

def remove_duplicates(arr):
    j = 1
    for i in range(1,len(arr)):
        if arr[i]!=arr[i-1]:
            arr[j]=arr[i]
            j+=1

    return j

arr = [1,2,3,3,4,4,5]
s = 5
print (remove_duplicates(arr))
