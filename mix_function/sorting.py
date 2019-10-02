# arr = list("omama")
# print(arr)
# print(sorted(arr))
# print(sorted(arr,reverse=True))


def sel_sort(arr):

    for i in range(len(arr)-1,0,-1):
        min_idx = 0
        for j in range(1,i+1):
            if arr[min_idx] < arr[j]:
                min_idx = j

        temp = arr[j]
        arr[j] = arr[min_idx]
        arr[min_idx] = temp
    return arr




def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

arr = [3,5,4,5]
print(bubbleSort(arr))




def factorial():
    zero = []
    a = 10
    # a = len(c)
    # i=1
    for i in range(a):
        zero.append(i)
    x = print(sum(zero[1:]))
    return x

factorial()

def try_map(n):
    n = n-1
    return n

n = [1,2,3]
print(list(map(try_map, n)))