def selection_sort(lyst):
    front = 0
    while front < len(lyst) - 1:
        min_idx = front
        item = min_idx + 1
        while item < len(lyst):
            if lyst[min_idx] > lyst[item]:
                min_idx = item
            item += 1
        if min_idx != front:
            lyst[min_idx], lyst[front] = lyst[front], lyst[min_idx]
        front += 1
    return lyst


print(selection_sort([5, 3, 1, 2, 4]))
