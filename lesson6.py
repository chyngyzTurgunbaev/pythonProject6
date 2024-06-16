def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
unsorted_list = [64, 34, 25, 12, 22, 11, 90,12]
print("Bubble Sorted list:", bubble_sort(unsorted_list.copy()))
def binary_search(arr, val):
    N = len(arr)
    ResultOk = False
    First = 0
    Last = N - 1
    Pos = -1

    while First < Last:
        Middle = (First + Last) // 2

        if val == arr[Middle]:
            ResultOk = True
            Pos = Middle
            break
        elif val > arr[Middle]:
            First = Middle + 1
        else:
            Last = Middle - 1

    if ResultOk:
        print("Элемент найден на позиции:", Pos)
    else:
        print("Элемент не найден")

# Пример использования
arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39]
val = 25
binary_search(arr, val)