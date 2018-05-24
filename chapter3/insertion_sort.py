def insertion_sort(lyst):
    i = 1
    while i < len(lyst):
        idx = i
        while idx > 0 and lyst[idx - 1] > lyst[idx]:
            lyst[idx - 1], lyst[idx] = lyst[idx], lyst[idx - 1]
            idx -= 1
        i += 1
    return lyst


print(insertion_sort([3, 2, 5, 1, 4]))
