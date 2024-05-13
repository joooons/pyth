import random


def array_of_int(min, max, n):
    arr = []
    for i in range(n):
        arr.append(random.randrange(min, max))
    return arr


def selection_sort(arr):
    n = len(arr)
    # 1 5 4 2 3
    for i in range(n-1):
        i_min = i
        for j in range(i+1, n):
            if (arr[j] < arr[i_min]):
                i_min = j
        [arr[i_min], arr[i]] = [arr[i], arr[i_min]]
    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]


def main():
    arr = array_of_int(0, 9, 5)
    print(arr)

    selection_sort(arr)
    bubble_sort(arr)
    print(arr)


if __name__ == "__main__":
    main()
