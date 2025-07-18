def divisions_int(n, b=1000):
    quotient = randint(1, b)

    for i in range(n):
        quotient //= randint(1, b)

    return quotient