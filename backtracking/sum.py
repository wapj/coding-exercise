def total(n, arr):
    if arr:
        n += arr[0]
        return total(n, arr[1:])
    else:
        return n


arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(total(0, arr))
