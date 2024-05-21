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


@show_time_duration
def merge_sort(arr):
    res = arr[:]

    def merge(arr):
        n = len(arr)
        if n <= 1:
            return arr
        arA = merge(arr[:n//2])
        arB = merge(arr[n//2:])
        [a, b] = [0, 0]
        for i in range(n):
            if a == len(arA):
                arr[i] = arB[b]
                b += 1
            elif b == len(arB):
                arr[i] = arA[a]
                a += 1
            elif (arA[a] < arB[b]):
                arr[i] = arA[a]
                a += 1
            else:
                arr[i] = arB[b]
                b += 1
        return arr
    return merge(res)


count = 0


@show_time_duration
def quick_sort(arr):
    def quick(arr):
        n = len(arr)
        if n < 2:
            return arr
        arr_L = []
        arr_R = []
        for i in range(n-1):
            if arr[i] < arr[n-1]:
                arr_L.append(arr[i])
            else:
                arr_R.append(arr[i])
        return quick(arr_L) + [arr[n-1]] + quick(arr_R)
    return quick(arr)


@show_time_duration
def custom_sort(arr):
    n = len(arr)
    res = arr[:]

    return res


def main():
    arr = array_of_int(0, 9, 5000)
    if len(arr) < 10:
        print('og: ', arr)

    # ss_arr = selection_sort(arr)
    # bs_arr = bubble_sort(arr)
    # is_arr = insertion_sort(arr)
    ms_arr = merge_sort(arr)
    # cs_arr = custom_sort(arr)
    qs_arr = quick_sort(arr)

    if len(arr) < 10:
        print("ms: ", ms_arr)
        print("qs: ", qs_arr)
    print("equal?: ", ms_arr == qs_arr)


if __name__ == "__main__":
    main()
