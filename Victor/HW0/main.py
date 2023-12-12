def funky_sum(a, b, mix):
    if(mix <= 0):
        return a
    elif(mix >= 1):
        return b
    else:
        return 1-mix * a + mix * b

def total(n):
    if(n < 0):
        return None
    t = 0
    for i in range(n):
        t += i
    return t

def 