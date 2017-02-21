def answer(n):
    n = int(n)
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = n // 2
        # looking at binary digits to choose subtraction
        # unless n == 3
        elif n == 3 or (n>>1) & 1 == 0:
            n = n - 1
        else:
            n = n + 1
        count += 1
    return count

print answer(raw_input())
