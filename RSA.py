import math
def gcd(a,b):
    while b:
        a, b=b,a % b
    return a
def generate_keypair(p,q):
    n= p * q
    phi= (p-1) * (q-1)
    e=17
    while gcd (e, phi)!=1:
      e+=2
    d = pow(e, -1,phi)
    return ((e,n),(d,n))
def encrypt(public_key,plaintext_mgs):
    e,n=public_key
    ciphertext=pow(plaintext_mgs,e,n)
    return ciphertext
def decrypt(ciphertext,private_key):
    d,n=private_key
    plaintext=pow(ciphertext,d,n)
    return plaintext
if __name__=="__main__":
    p=3
    q=11
    public_key,private_key=generate_keypair(p,q)
    print(f"public key:{public_key}")
    print(f"private key:{private_key}")
    mgs=6
    encrypted_mgs=encrypt(public_key,mgs)
    print(f"encrypted msg:{encrypted_mgs}")
    decrypted_mgs=decrypt(encrypted_mgs,private_key)
    print(f"decrypted mgs:{decrypted_mgs}")
        