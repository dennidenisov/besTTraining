#Алгоритм Сортировки

array = [3, 1, 6, 4]
# определяем длину массива
length = len(array)
#Внешний цикл, количество проходов N-1
for i in range(length):
    # Внутренний цикл, N-i-1 проходов
    for j in range(0, length-i-1):
        #Меняем элементы местами
        if array[j] > array[j+1]:
            temp = array[j]
            array[j] = array[j+1]
            array[j+1] = temp