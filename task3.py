import random


def main():
    array = [random.randint(-100, 100) for _ in range(10)]
    print(array)

    array = merge_sort(array)
    print(array)


def merge_sort(array: list) -> list:
    half_len = len(array) >> 1

    if not half_len:
        return array

    array0 = array[:half_len]
    array1 = array[half_len:]

    array0 = merge_sort(array0)
    array1 = merge_sort(array1)

    ret = []

    while array0 or array1:
        if array0 and array1:
            if array0[0] <= array1[0]:
                ret.append(array0.pop(0))
            else:
                ret.append(array1.pop(0))
        elif array0:
            ret.append(array0.pop(0))
        else:
            ret.append(array1.pop(0))

    return ret


if __name__ == "__main__":
    main()
