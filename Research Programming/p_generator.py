import time

def isPrime(n):
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def is2PrimitiveRootOfP(p):
    """
    If ordp(2) = p-1
    First time 2^k % p = 1 is when k = p-1
    """

    # Must be prime
    if not isPrime(p):
        return False

    # 1 ... p-1
    for k in range(1, p):
        if (2 ** k) % p == 1:
            if k == p-1:
                return True
            else:
                return False
    return False

def findPValues(upper, lower=1):
    ret = []
    for p in range(lower, upper+1):
        if is2PrimitiveRootOfP(p):
            ret.append(p)
    return ret


if __name__ == '__main__':
    start = time.time()
    print(findPValues(10000))
    end = time.time()
    print(f"{(end - start):.2f} seconds")
