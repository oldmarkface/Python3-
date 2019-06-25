def find_smallest(arr):
    # 获取最小元素的小表
    smallest = arr[0]
    smallest_index = 0
    for index in range(1, len(arr)):
        if arr[index] < smallest:
            smallest = arr[index]
            smallest_index = index
    return smallest_index


def selection_sort(arr):
    # 选择排序
    new_arr = []
    for index in range(len(arr)):
        smallest = find_smallest(arr)
        new_arr.append(arr.pop(smallest))
    return new_arr


if __name__ == '__main__':
    print(selection_sort([1, 3, 5, 4, 7, 9, 2, 8]))
