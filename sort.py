import random
import time


def show_time_duration(func):
    def wrapper(*args):
        start = time.time() * 1000
        res = func(*args)
        end = time.time() * 1000
        print('{0}() took {1:.0f} ms'.format(func.__name__, end - start))
        return res
    return wrapper


@show_time_duration
def array_of_int(min, max, n):
    arr = []
    for i in range(n):
        arr.append(random.randrange(min, max))
    return arr


@show_time_duration
def selection_sort(arr):
    n = len(arr)
    res = arr[:]
    for i in range(n-1):
        i_min = i
        for j in range(i+1, n):
            if (res[j] < res[i_min]):
                i_min = j
        [res[i_min], res[i]] = [res[i], res[i_min]]
    return res


@show_time_duration
def bubble_sort(arr):
    n = len(arr)
    res = arr[:]
    for i in range(n):
        for j in range(n-i-1):
            if res[j] > res[j+1]:
                res[j], res[j+1] = res[j+1], res[j]
    return res


@show_time_duration
def insertion_sort(arr):
    n = len(arr)
    res = arr[:]
    # 1 5 3 4 2
    for i in range(n):
        j = i
        while j > 0 and res[j-1] > res[j]:
            [res[j-1], res[j]] = [res[j], res[j-1]]
            j -= 1
    return res


# @show_time_duration
def merge_sort(arr):
    n = len(arr)
    res = arr[:]

    if n <= 1:
        return res

    arA = merge_sort(res[:n//2])
    arB = merge_sort(res[n//2:])
    print(f'merge {arA} :: {arB}')

    [a, b] = [0, 0]
    for i in range(n):
        if a == len(arA):
            res[i] = arB[b]
            b += 1
        elif b == len(arB):
            res[i] = arA[a]
            a += 1
        elif (arA[a] < arB[b]):
            res[i] = arA[a]
            a += 1
        else:
            res[i] = arB[b]
            b += 1

    return res


@show_time_duration
def custom_sort(arr):
    n = len(arr)
    res = arr[:]

    return res


def main():
    arr = array_of_int(0, 9, 7)
    print(arr)
    # a = [1]
    # b = [1, 5]
    # c = [1, 5, 2]
    # d = [1, 5, 2, 6]

    # ss_arr = selection_sort(arr)
    # bs_arr = bubble_sort(arr)
    # is_arr = insertion_sort(arr)
    # ms_arr = merge_sort(a)
    # ms_arr = merge_sort(b)
    # ms_arr = merge_sort(c)
    # ms_arr = merge_sort(d)
    ms_arr = merge_sort(arr)
    print(ms_arr)
    # cs_arr = custom_sort(arr)


if __name__ == "__main__":
    main()
