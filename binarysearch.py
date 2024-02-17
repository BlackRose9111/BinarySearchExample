from random import randint

def fill_an_array(n):
    return [randint(0, 1000) for _ in range(n)]

def sort_an_array(arr):
    return sorted(arr)

def fill_an_array_with_sequential_numbers(n):
    return [i for i in range(n)]


def binary_search(arr, x):
    left,right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return -1

def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


def main():
    arr = fill_an_array_with_sequential_numbers(1000) #fill_an_array(10000)
    print(arr)
    arr = sort_an_array(arr)
    print(arr)
    x = 10000
    result1 = binary_search(arr, x)
    result2 = linear_search(arr, x)
    t = f"Binary search: {result1} Linear search: {result2}"
    print(t)

if __name__ == "__main__":
    main()
