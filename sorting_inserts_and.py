def sorting_inserts_and(spisok):
    # Функция сортирует список (он же массив) от меньшего к большему
    # в параметрах функции spisok - это список который нужно отсортировать


    for i in range(1, len(spisok)):
        present_value = spisok[i]
        position = i
        while position > 0 and spisok[position - 1] > present_value:
            spisok[position] = spisok[position - 1]
            position = position - 1
            spisok[position] = present_value

    return spisok

s = [8, 2, 1, 3, 5, 4, 6, 7]
print(sorting_inserts_and(s))