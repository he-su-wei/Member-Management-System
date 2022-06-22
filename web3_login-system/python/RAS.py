import sympy
import numpy as np

# 隨機產生 512 位元的質數
def generate_prime():
    prime = sympy.randprime(2**511, 2**512)
    return prime

def pubKey_priKey():

    p = generate_prime()
    q = generate_prime()
    print('p = ', p, '\nq=', q)
    print(type(p))


    # 計算 N = p*q
    n = p * q
    print('mod(n) = ', n)

    # 根據歐拉函數，求得phi_n = phi(p)*phi(q) = (p - 1)(q - 1)
    phi_n = (p-1) * (q-1)
    print("phi_n", phi_n)

    # 選一個小於 phi_n 的整數 e，且 phi_n 與 e 互質。
    e = sympy.randprime(phi_n // 2, phi_n)
    print('公鑰 e =', e)

    # 並求得 e 關於 phi_n 的反模元素
    d, _, gcd = sympy.gcdex(e, phi_n)
    if gcd != 1:
        print('gcd(e, phi_n) != 1 錯')
    d = (d + phi_n) % phi_n
    print("私鑰 d = ", d)

    return(n, e, d)

    # print(e * d % phi_n == 1) True:代表模反元素存在，若且唯若e 與 phi_n 互質

#----------------------------------------

plaintext = '109021372 何書維'
m = plaintext.encode('utf-8')

mm = int.from_bytes(m, byteorder='little')
print(len(m))
print(mm<n)
print(mm)


def mod_powLSB(x, exp, n):
    y = 1
    x = x % n
    while exp > 0:
        if (exp % 2 == 1):
            y = (y * n) % n
        exp = exp // 2
        x == (x * x) % n
    return y

def mod_powMSB(x, exp, n):
    e = bin(exp)[2:]
    print(e)
    y = 1
    for i in range(len(e)):
        y = (y * y) % n
        if e[i] == '1':
            y = y * x % n
    return y

cc = mod_powMSB(mm, e, n)
print(cc)

m2 = mod_powMSB(cc, d, n)
print(mm == m2)

sz = int(np.ceil(m2.bit_length()/8))
mm2 = int.to_bytes(m2, sz, byteorder='little')
print(mm2.decode('utf-8'))