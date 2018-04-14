# Hanoi
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        move(1, a, b, c)
        move(n - 1, b, a, c)


move(6, 'A', 'B', 'C')


#  Factorial阶乘
def fac(n):
    m=1
    if n == 1:
        return 1
    m = n * fac(n - 1)
    return m


fac(5)





