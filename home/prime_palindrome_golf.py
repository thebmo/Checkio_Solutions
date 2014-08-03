def g(n):
    while(n):
        n,p=n+1,1
        for i in range((n-1),1,-1):
            if n%i==0:p=0
        if p and pd(str(n)):return n
def pd(n):
    d,l=0 if len(n)%2==0 else 1,len(n)/2
    if n[:l+d]==n[l:][::-1]:return True
assert g(2) == 3
assert g(10) == 11
assert g(13) == 101
assert g(101) == 131