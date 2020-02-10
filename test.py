l = [1, 3, 4, 5]

def p1(n):
    n = n**n
    return n

l = map(p1, l)

print(l)
