def bubble_sort(lyst):
    rear = len(lyst) - 1
    while rear > 0:
        front = 0
        while front < rear:
            if lyst[front] > lyst[front + 1]:
                lyst[front], lyst[front + 1] = lyst[front + 1], lyst[front]
            front += 1
        rear -= 1
    return lyst


def short_bubble_sort(lyst):
    rear = len(lyst) - 1
    while rear > 1:
        swaped = False
        front = 0
        while front < rear:
            if lyst[front] > lyst[front + 1]:
                lyst[front], lyst[front + 1] = lyst[front + 1], lyst[front]
                swaped = True
            front += 1
        if not swaped:
            return lyst
        rear -= 1
    return lyst


print(bubble_sort([3, 2, 1]))
print(short_bubble_sort([5, 4, 2, 1, 3]))
