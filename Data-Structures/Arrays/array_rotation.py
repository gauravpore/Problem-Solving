#program for array rotation by d elements

def rotate_array(arr,d):
    temp = arr[:d]
    new = arr[d:]
    arr = new + temp
    return arr

arr = [ 1,2,3,4]
print (rotate_array(arr,1))

#method 2
def left_rotate(arr,d):
    for i in range (d):
        rotate_one(arr)


def rotate_one(arr):
    temp = arr[0]
    for i in range(len(arr)-1):
        arr[i]= arr[i+1]
    arr[len(arr)-1]= temp

def print_array(arr):
    for i in arr:
        print (i)

left_rotate(arr,2)
print_array([arr])
