import random
import time


def array_of_int(min, max, n):
    start = time.time() * 1000
    arr = []
    for i in range(n):
        arr.append(random.randrange(min, max))
    end = time.time() * 1000
    print('array_of_int() took {} ms'.format(end - start))
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
    print('selection_sort took {} ms'.format(end - start))
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
    print('selection_sort took {} ms'.format(end - start))
    return res


def main():
    arr = array_of_int(0, 9, 1000)
    # print(arr)

    ss_arr = selection_sort(arr)
    bs_arr = bubble_sort(arr)
    # print(arr)
    # print(ss_arr)
    # print(bs_arr)


if __name__ == "__main__":
    main()
