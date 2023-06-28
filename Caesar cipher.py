def caesar(n):
    d = {}
    for i in range (65,91):
        d[chr(i)] = chr(i+n)
    for i in range (97,123):
        d[chr(i)] = chr(i+n)
    return d

