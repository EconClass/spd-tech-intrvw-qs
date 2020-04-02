# We have to rotate the elements of the given array k times to the right.
# nums =  [3, 7, 1, 2] + [8, 5]

# [1,2 ,3] 3 ---> [3, 2, 1]

# k = 2

# # Expected output
# result = [1, 2, 8, 5, 3, 7]


def rotate(list_nums, k):
    last = len(list_nums)

    if last == 1 or last == k or last == 0:
        return list_nums
    elif k < 0:
        k = 0 - k  # make positive for indexing
        front = list_nums[k: last]
        back = list_nums[0: k]
        front.extend(back)
        return front
    else:
        front = list_nums[last - k:last]
        back = list_nums[0: last - k]
        front.extend(back)
        return front


if __name__ == "__main__":
    given = [8, 5, 3, 7, 1, 2]
    # Normal Cases
    print(given)
    print(rotate(given, -2))

    # Edge Cases
    print(given)
    print(rotate([8, 5, 3, 7, 1, 2], 6))

    given = [1, 2]
    print(given)
    print(rotate([1, 2], -1))
