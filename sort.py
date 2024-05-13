import random
import time


def array_of_int(min, max, n):
    start = time.time() * 1000
    arr = []
    for i in range(n):
        arr.append(random.randrange(min, max))
    end = time.time() * 1000
    print('array_of_int() took {0:.0f} ms'.format(end - start))
    return arr


def selection_sort(arr):
    start = time.time() * 1000
    n = len(arr)
    res = arr[:]
    for i in range(n-1):
        i_min = i
        for j in range(i+1, n):
            if (res[j] < res[i_min]):
                i_min = j
        [res[i_min], res[i]] = [res[i], res[i_min]]
    end = time.time() * 1000
    print('selection_sort took {0:.0f} ms'.format(end - start))
    return res


def bubble_sort(arr):
    start = time.time() * 1000
    n = len(arr)
    res = arr[:]
    for i in range(n):
        for j in range(n-i-1):
            if res[j] > res[j+1]:
                res[j], res[j+1] = res[j+1], res[j]
    end = time.time() * 1000
    print('bubble_sort took {0:.0f} ms'.format(end - start))
    return res


def insertion_sort(arr):
    start = time.time() * 1000
    n = len(arr)
    res = arr[:]
    # 1 5 3 4 2
    for i in range(n):
        j = i
        while j > 0 and res[j-1] > res[j]:
            [res[j-1], res[j]] = [res[j], res[j-1]]
            j -= 1
    end = time.time() * 1000
    print('insertion_sort took {0:.0f} ms'.format(end - start))
    return res


def merge_sort(arr):
    start = time.time() * 1000
    n = len(arr)
    res = arr[:]

    end = time.time() * 1000
    print('merge_sort tooke {0:.0f} ms'.format(end - start))
    return res


def custom_sort(arr):
    start = time.time() * 1000
    n = len(arr)
    res = arr[:]

    end = time.time() * 1000
    print('custom_sort took {} ms'.format(end - start))
    return res


def main():
    arr = array_of_int(0, 9, 2000)
    # print(arr)

    ss_arr = selection_sort(arr)
    bs_arr = bubble_sort(arr)
    is_arr = insertion_sort(arr)
    cs_arr = custom_sort(arr)
    # print(arr)
    # print(ss_arr)
    # print(bs_arr)


if __name__ == "__main__":
    main()
