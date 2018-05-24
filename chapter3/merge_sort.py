def merge_sort(lyst):
    if len(lyst) > 1:
        mid = len(lyst) // 2
        front_half = lyst[:mid]
        rear_half = lyst[mid:]
        merge_sort(front_half)
        merge_sort(rear_half)
        i, j, idx = 0, 0, 0
        while i < len(front_half) and j < len(rear_half):
            if front_half[i] < rear_half[j]:
                lyst[idx] = front_half[i]
                i += 1
            elif front_half[i] > rear_half[j]:
                lyst[idx] = rear_half[j]
                j += 1
            idx += 1
        while i < len(front_half):
            lyst[idx] = front_half[i]
            idx += 1
            i += 1
        while j < len(rear_half):
            lyst[idx] = rear_half[j]
            idx += 1
            j += 1


lyst = [4, 1, 7, 6, 5, 3, 8, 2]
merge_sort(lyst)
print(lyst)
