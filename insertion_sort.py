lst = [2,1,2,5,2,56,3,6,6,7,2,4,27,7,9,0]

def insertion_sort(lst):

    length = len(lst)
    

    for i in range(length):

        j = i - 1
        key = lst[i]

        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1

        lst[j + 1] = key

        
        




    return lst

# print(insertion_sort(lst))


def selectionSort(lst):

    length = len(lst)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if lst[j] < lst[min_index]:
                min_index = j

        lst[i], lst[min_index] = lst[min_index], lst[i]

    return lst

# print(selectionSort(lst))
# 2
# 2 1
# 1 2 2


data =[[1, 2],[3, 4],[5, 6]]

row =data[1]

row[0] =99
print(data)
data[2] =data[0]
print(data)
data[0][1]= 88

print(data)