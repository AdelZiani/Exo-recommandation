def premier4(n):
    if n == 2:
        return True
    if n == 0 or n == 1 or (n % 2) == 0:
        return False
    for div in range(3, int(sqrt(n)) + 1, 2):
        if n % div == 0:
            return False

    return True