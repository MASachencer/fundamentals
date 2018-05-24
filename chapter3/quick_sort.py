def partition(lyst, first, last):
    mid = (first + last) // 2
    left = first + 1
    right = last
    for idx in range(mid + 1, right):
        if lyst[idx] < lyst[first]:
            lyst[idx], lyst[left] = lyst[left], lyst[idx]
            left += 1
    lyst[first], lyst[mid] = lyst[mid], lyst[first]
    return first


def quick_sort_helper(lyst, first, last):
    if first < last:
        pivot = partition(lyst, first, last)
        quick_sort_helper(lyst, first, pivot - 1)
        quick_sort_helper(lyst, pivot + 1, last)


def quick_sort(lyst):
    quick_sort_helper(lyst, 0, len(lyst) - 1)


lyst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(lyst)
print(lyst)
