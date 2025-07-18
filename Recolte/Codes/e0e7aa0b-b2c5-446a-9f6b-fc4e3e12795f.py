def count_ids(filename):
    ids = set()
    with open(filename, 'r') as f:
        for line in f:
            values = line.split(sep=' ')
            ids.add(values[0])
            ids.add(values[1])
    return len(ids)