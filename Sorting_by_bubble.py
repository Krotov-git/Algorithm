def sorting_by_bubble(spisok):
#Функция сортирует список (он же массив) от меньшего к большему
# в параметрах функции spisok - это список который нужно отсортировать

    spisok = spisok.copy()
    l = len(spisok)

    for i in range(l - 1):
        for j in range(l - i - 1):
            if spisok[j] > spisok[j + 1]:
                spisok[j], spisok[j + 1] = spisok[j + 1], spisok[j]
    return spisok

s = [8, 2, 1, 3, 5, 4, 6, 7]
print(sorting_by_bubble(s))