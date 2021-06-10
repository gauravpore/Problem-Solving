#program for selection sort
def selection_sort(A): #O(n^2)
  for i in range (len(A)):
    min_idx = i #index of smallest element
    for j in range(i+1,len(A)):
        if A[min_idx]>A[j]:
            min_idx = j
    A[i],A[min_idx] = A[min_idx],A[i]
  return A

def bubble_sort(A):
    n = len(A)
    for i in range(n-1):
        swapped = False
        for j in range(n-1-i):
            if A[j]>A[j+1]:
                A[j],A[j+1]=A[j+1],A[j] #swapping
                swapped = True
        if swapped==False:
            break
    return A

def insertion_sort(A):
    for i in range(1,len(A)):
        j = i -1 #prev index of current element
        while A[j]>A[j+1] and j>=0:
            A[j],A[j+1]=A[j+1],A[j]
            j =-1
    return A

def quick_sort(arr):
    if len(arr)<2:
        return arr
    pivot = arr[0]
    cur = 0

    for i in range(1,len(arr)):
        if arr[i]<pivot:
            cur+=1
            arr[cur],arr[i]=arr[i],arr[cur]
    arr[0],arr[cur]=arr[cur],arr[0]
    left = quick_sort(arr[:cur])
    right = quick_sort(arr[cur+1:])
    return left + [arr[cur]] + right

def mergeSort(arr):
    if len(arr) > 1:
        # Finding the mid of the array
        mid = len(arr) // 2
        # Dividing the array elements
        L = arr[:mid]
        # into 2 halves
        R = arr[mid:]
        # Sorting the first half
        mergeSort(L)
        # Sorting the second half
        mergeSort(R)
        i = j = k = 0
        # Copy data to temp arrays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1
        # Checking if any element was left
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

#Driver-code
A = [23,45,11,22,54]
print (selection_sort(A))
print (bubble_sort(A))
print (insertion_sort(A))
print (quick_sort(A))
print (mergeSort(A))
