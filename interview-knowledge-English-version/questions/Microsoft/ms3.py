def findWords(matrix):
    row, col = len(matrix), len(matrix[0])
    return


def halfSearch(arr, left, right, target):
    middle = (left + right) // 2
    while left <= right:
        middle = (right - left) // 2 + left
        if arr[middle] == target:
            return middle
        if arr[middle] < target:
            left = middle+1
        if arr[middle] > target:
            right = middle-1

    return -1


def findDemarcation(arr, target):
    length = len(arr)
    left, right = 0, length-1
    middle = (right + left) // 2
    while left <= right:
        middle = (right - left) // 2 + left
        if arr[middle] > arr[middle + 1] and arr[middle] > arr[middle + 1]:
            break
        if arr[middle] < arr[middle + 1]:
            left = middle+1
        if arr[middle] < arr[middle - 1]:
            right = middle-1
    left1, right1 = 0, middle+1
    left2, right2 = middle, length-1
    ans1 = halfSearch(arr, left1, right1, target)
    if ans1 == -1:
        return halfSearch(arr, left2, right2, target)
    return ans1


if __name__ == '__main__':
    arr_test = [2, 3, 4, 8, 10, 100, 9, 5, 1]
    print(findDemarcation(arr_test, 5))
