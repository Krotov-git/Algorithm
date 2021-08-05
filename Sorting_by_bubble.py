def bubble_sort(arr):
    '''
    Функция сортирует массив от наименьшего к наибольшему
    :param arr - список из элементов который нужно отсортировать
    '''

    arr = arr.copy()
    L = len(arr)

    for i in range(L - 1):
        for j in range(L - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

s = [8, 2, 1, 3, 5, 4, 6, 7]
print(bubble_sort(s))