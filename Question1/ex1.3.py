


def fibmemo(n, cache={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fibmemo(n-1) + fibmemo(n-2)
            return cache[n]

