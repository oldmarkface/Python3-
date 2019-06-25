def binary_search(the_list, item):
    # 二分法查找
    low = 0
    height = len(the_list)

    while low < height:
        mid = int((height + low) / 2)
        guess = the_list[mid]
        if guess > item:
            height = mid
        elif guess < item:
            low = mid
        else:
            return mid
    return None


if __name__ == '__main__':
    result=binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    print(result)
