def is_factor(n, m):
    if n == 0:
        return False
    elif m == 0:
        return False
    else:       
        return not (m % n)

