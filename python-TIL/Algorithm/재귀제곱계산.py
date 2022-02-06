tap = ' '
def pow(x, n):
    global tap
    tap += ' '
    if n == 0:
        return 1
    print(tap + "%d * %d^(%d-%d)" % (x, x, n, 1 ))
    return x * pow(x, n-1)

print('2^4')
print('답-->', pow(2,4))