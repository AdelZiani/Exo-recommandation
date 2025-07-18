def count_lines(filename):
    with open(filename, newline='') as f:
        n = 0
        for line in f:
            n += 1
    return n