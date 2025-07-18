def print_main_callers(filename, n):
    d = dict()
    with open(filename, 'r') as f:
        for i in f.readlines():
            caller_id, _, _, _ = i.split()
            d[caller_id] = d.get(caller_id, 0) + 1
    main_callers = [i for i in sorted(d.items(), key = lambda item : item[1], reverse = True)]
    for i in range(min(n, len(main_callers))):
        print(main_callers[i])