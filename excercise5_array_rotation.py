#!/usr/bin/env python3

def rotate_temp_array(vect, k):
    n = len(vect)
    if n == 0:
        return vect

    k = k % n
    return vect[-k:] + vect[:-k]


def rotate_one_by_one(vect, k):
    n = len(vect)
    if n == 0:
        return vect

    k = k % n

    for _ in range(k):
        last = vect[-1]
        for i in range(n - 1, 0, -1):
            vect[i] = vect[i - 1]
        vect[0] = last

    return vect


def reverse(vect, start, end):
    while start < end:
        vect[start], vect[end] = vect[end], vect[start]
        start += 1
        end -= 1


def rotate_reverse_method(vect, k):
    n = len(vect)
    if n == 0:
        return vect

    k = k % n

    reverse(vect, 0, n - 1)
    reverse(vect, 0, k - 1)
    reverse(vect, k, n - 1)

    return vect


if __name__ == "__main__":
    test_vect = [1, 2, 3, 4, 5, 6, 7]
    k = 10

    print("Original:", test_vect)

    print("\nUsing temporary array:")
    print(rotate_temp_array(test_vect.copy(), k))

    print("\nRotate one by one:")
    print(rotate_one_by_one(test_vect.copy(), k))

    print("\nReverse method (optimal):")
    print(rotate_reverse_method(test_vect.copy(), k))

    print("\nEdge Case: Single Element")
    single_vect = [1]
    k_edge = 5
    print("Input:", single_vect, "k =", k_edge)
    print("Output:", rotate_reverse_method(single_vect.copy(), k_edge))
