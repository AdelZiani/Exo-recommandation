def premier3(n):
    if n == 2:
        return True
    if n == 0 or n == 1:
        return False
    for div in range(2, int(sqrt(n)) + 1):
        if n % div == 0:
            return False

    return True