def insertion_sort(lyst):
    front = 1
    while front < len(lyst):
        rear = front
        while rear > 0 and lyst[rear - 1] > lyst[rear]:
            lyst[rear - 1], lyst[rear] = lyst[rear], lyst[rear - 1]
            rear -= 1
        front += 1
    return lyst

print(insertion_sort([3, 2, 5, 1, 4]))
