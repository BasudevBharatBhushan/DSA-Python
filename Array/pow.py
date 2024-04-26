# Power

def myPow(x:float, n:int)-> float:
    ans = 1.0

    nn = n

    if nn < 0:
        nn = -1 * nn

    while nn:
        if nn & 1 == 1:  # if nn is odd
            ans *= x
            nn -= 1
        else:
            x *= x
            nn //= 2
    
    if n < 0:
        ans = 1.0/ans

    return ans


'''

2 ^ 10 = (2 * 2) ^ 5

'''

# Test Cases
x = 2
n = 10
print(myPow(x, n)) # 1024.0