def expo(num, p):
    count = 1
    for n in range(p):
        count *= num
    return count


print(expo(2, 2))
