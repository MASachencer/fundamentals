def bubble_sort(lyst):
    length = len(lyst) - 1
    while length > 0:
        item = 0
        while item < length:
            if lyst[item] > lyst[item + 1]:
                lyst[item], lyst[item + 1] = lyst[item + 1], lyst[item]
            item += 1
        length -= 1
    return lyst


def short_bubble_sort(lyst):
    length = len(lyst) - 1
    while length > 1:
        swaped = False
        item = 0
        while item < length:
            if lyst[item] > lyst[item + 1]:
                lyst[item], lyst[item + 1] = lyst[item + 1], lyst[item]
                swaped = True
            item += 1
        if not swaped:
            return lyst
        length -= 1
    return lyst


print(bubble_sort([3, 2, 1]))
print(short_bubble_sort([5, 4, 2, 1, 3]))
