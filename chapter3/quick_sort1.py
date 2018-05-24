def quick_sort(lyst):
    quick_sort_helper(lyst, 0, len(lyst) - 1)


def quick_sort_helper(lyst, first, last):
    if first < last:
        pivot = partition(lyst, first, last)
        quick_sort_helper(lyst, first, pivot - 1)
        quick_sort_helper(lyst, pivot + 1, last)


def partition(lyst, first, last):
    left = first
    right = last
    while left < right:
        while lyst[left] < lyst[first]:
            left += 1
        while lyst[right] > lyst[first]:
            right -= 1
        lyst[left], lyst[right] = lyst[right], lyst[left]
    lyst[first], lyst[left] = lyst[left], lyst[first]
    return left


lyst = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(lyst)
print(lyst)
