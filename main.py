from Prime import miller_rabin_test, fast_raising_to_a_power, is_coprime
from ASCII import to_text, to_ascii
from Congruence import modinv

# First Step - Creation of message M and converting it to ASCII
M = str(input('Define alphanumeric message M, M='))
M_ASCII = to_ascii(M)
print(M_ASCII)

# Second Step - defining prime secret key "p"
b = 0
while b < 1 :
    p = int(input('Define secret prime key p, p='))
    b = miller_rabin_test(2, p)


# Third step - defining eA and calculating dA
eA = 0 # for purpose of following loop
b = 0
while eA < 2 or eA > p-2 or b == 0:
    eA = int(input('Define encryption key that satisfies conditions (1 < eA < p-1) and eA is co-prime with p-1, eA='))
    b = is_coprime(eA, p-1)
    if eA < 2 or eA > p-2:
        print("Defined eA key exceeded it's possible range of (1,p-1)")
    elif b == 0:
        print("Defined eA key is not co-prime with p-1")
    else:
        print("Defined eA key is ", eA)
    dA = modinv(eA, p-1)
    print("Decryption key dA for given eA is equal ", dA)


# Fourth Step - Generating and sending C1
C1 = []
for c in M_ASCII: C1.append(fast_raising_to_a_power(c, eA, p))
print(C1)
'#print(to_text(C1))


# Fifth Step - Bob defines dB and eB is calculated
dB = 0 # for purpose of following loop
b = 0
while dB < 2 or dB > p-2 or b == 0:
    dB = int(input('Define decryption key that satisfies conditions (1 < dB < p-1) and dB is co-prime with p-1, dB='))
    b = is_coprime(dB, p-1)
    if dB < 2 or dB > p-2:
        print("Defined dB key exceeded it's possible range of (1,p-1)")
    elif b == 0:
        print("Defined dB key is not co-prime with p-1")
    else:
        print("Defined dB key is ", dB)
    eB = modinv(dB,p-1)
    print("Encryption key dA for given eA is equal ", eB)


# Sixth Step - Bob generates C2
C2 = []
for c in C1: C2.append(fast_raising_to_a_power(c, dB, p))
print(C2)


# Seventh Step - Alice receives C2 and generate C3
C3 =[]
for c in C2: C3.append(fast_raising_to_a_power(c, dA, p))
print(C3)


# Eighth Step - Bob receives C3 which is final message. In this step Bob will decipher C3 in order to obtain M
M_received =[]
for c in C3: M_received.append(fast_raising_to_a_power(c, eB, p))
print(M_received)
print(to_text(M_received))