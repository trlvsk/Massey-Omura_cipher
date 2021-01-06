#Test pierwszoÅ›ci Millera-Rabina

def gcd(p, q):
    # Create the gcd of two positive integers.
    while q != 0:
        p, q = q, p % q
    return p


def is_coprime(x, y):
    return gcd(x, y) == 1

def fast_raising_to_a_power(a,k,n):
    b=1
    while k!=0:
        k_i=k%2
        k=k//2
        b=(b*(a**k_i))%n
        a=(a*a)%n
    return b

# koniec definicji funkcji fast_raising_to_a_power(a,k,n)

def miller_rabin_test(t,n):
    import random
    n_1=n-1
    s=0
    d=n_1
    while (d%2)==0:
        d=d//2
        s=s+1
# koniec obliczania s i d takich, Å¼e n-1=(2**s)*d,
# gdzie d jest nieparzystÄ… liczbÄ… naturalnÄ… a s jest liczbÄ… naturalnÄ…

    for i in range(t):              # pÄ™tla t eksperymentÃ³w (prÃ³b Bernoulliego)
        pseudop=0
        a=random.randrange(2,n_1,1) # losowy wybÃ³r podstawy potÄ™gi

        #print(a)

        #y=1
        #for k in range(d):          # obliczamy y=(a**d)%n
        #    y=(y*a)%n

        y=fast_raising_to_a_power(a,d,n)

        print(y)

        if y!=1 and y!=n_1:
            j=1
            while j<s:
                y=(y*y)%n
                if y==n_1:
                    pseudop=1
                    exit
                j=j+1
        else:
            pseudop=1

        if pseudop==0:
            return(0) # not prime

    return(1)  # prime



