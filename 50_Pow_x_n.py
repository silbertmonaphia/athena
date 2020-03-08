# Divide and Conquer(Recursive)
def myPow(x,n):
    # break
    if not n:
        return 1
    if n < 0:
        return 1 / myPow(x, -n)
    if n % 2:
        return x * myPow(x, n - 1)
    return myPow(x*x, n/2)

def myPow(x,n):
    if n < 0:
        x = 1 / x
        n = -n
    pow = 1
    while n:
        if n & 1:
            # Cpp prefer Bitwise operation
            pow *= x
        x *= x
        n >>= 1
    return pow