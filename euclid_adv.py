def euclid_gcd(n:int, p:int):
    """
    Extended Euclidean algorithm
    
    Parameters
    ----------
    n : int
        n*x ≡ 1 (mod p)
    p : int
        n*x ≡ 1 (mod p)

    returns
    ----------
    x : int
        n*x ≡ 1 (mod p)
    """
    left:list=list() # left side
    right:list=list() # right side
    left.append(p)
    right.append(0)
    left.append(n)
    right.append(1)
    index=1
    while left[index]!=1:
        k = left[index-1]//left[index]
        left.append(left[index-1] - left[index]*k)
        right.append(right[index-1] -right[index]*k)
        index+=1
    return right[index] if right[index] > 0 else p+right[index]

print(euclid_gcd(64, 83))