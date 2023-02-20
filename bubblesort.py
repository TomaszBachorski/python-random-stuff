arr = [1, 100, 2, 3, 6, 1, 23, 24]


def sort (arr):
    for i in range(0, len(arr)):
        for j in range (i, len(arr)):
            if (arr[i] > arr[j]): 
                temp = arr[j]
                arr[j] = arr[i]
                arr[i] = temp
    return arr

arr = sort(arr)
print(arr)