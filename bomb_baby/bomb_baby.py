def check(m,f):
    if m % 2 == 0 and f % 2 == 0:
        return False
    if m == f:
        return False
    if m <= 0 or f <= 0:
        return False
    if m > 1 and f % m == 0:
        return False
    if f > 1 and m % f == 0:
        return False
    return True

def answer(m,f):
    m = (int(m))
    f = (int(f))

    counter = 0
    while m != 0 and f != 0:
        if not check(m,f):
            return "impossible"
        p = [m,f]
        if m > f:
            counter += (m-1)/f
            m %= f
        elif f > m:
            counter += (f-1)/m
            f %= m
        print m,f
    return str(counter)

m,f = raw_input().strip().split()
print answer(m,f)
