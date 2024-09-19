# hometask - 6

def bubble_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(n):
        for j in range(0, n-i-1):
            if unsorted_list[j] > unsorted_list[j+1]:
                unsorted_list[j], unsorted_list[j+1] = unsorted_list[j+1], unsorted_list[j]
    return unsorted_list

def binary_search(unsorted_list, target):
    low = 0
    high = len(unsorted_list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = unsorted_list[mid]

        if guess == target:
            return mid  
        elif guess > target:
            high = mid - 1  
        else:
            low = mid + 1  

    return None  

unsorted_list = [64, 34, 25, 12, 22, 11, 90]

sorted_list = bubble_sort(unsorted_list)
print(f"Отсортированный список: {sorted_list}")

target = 22
result = binary_search(sorted_list, target)

if result is not None:
    print(f"Элемент {target} найден на индексе {result}")
else:
    print(f"Элемент {target} не найден")
