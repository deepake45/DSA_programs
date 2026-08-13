""" question 3
selection sort"""

def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1,n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i],arr[min_index] = arr[min_index],arr[i]
    return arr

a = int(input("Enter the no of elements of the array : "))
arr = []
for k in range(a):
    b = int(input("Enter the elements of the array : "))
    arr.append(b)
print("Original Array  : ",arr)
sorted_array = selection_sort(arr)
print("Sorted Array : ",sorted_array)
