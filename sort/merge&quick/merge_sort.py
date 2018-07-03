def merge_sort(lyst):
    if len(lyst) > 1:
        mid = len(lyst) // 2
        front_half = lyst[:mid]
        rear_half = lyst[mid:]
        merge_sort(front_half)
        merge_sort(rear_half)
        f_idx, r_idx, idx = 0, 0, 0
        while f_idx < len(front_half) and r_idx < len(rear_half):
            if front_half[f_idx] < rear_half[r_idx]:
                lyst[idx] = front_half[f_idx]
                f_idx += 1
            elif front_half[f_idx] > rear_half[r_idx]:
                lyst[idx] = rear_half[r_idx]
                r_idx += 1
            idx += 1
        while f_idx < len(front_half):
            lyst[idx] = front_half[f_idx]
            idx += 1
            f_idx += 1
        while r_idx < len(rear_half):
            lyst[idx] = rear_half[r_idx]
            idx += 1
            r_idx += 1
    return lyst


lyst = [4, 1, 7, 6, 5, 3, 8, 2]
print(merge_sort(lyst))
