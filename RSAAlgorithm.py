# July 2021
# RSA public key cipher implementation in Python that asks for number 1 and number 2 and checks to make sure they are both prime. The user then enters an exponent and makes sure that it is a coprime of phi of mod according to the algorithm. The plaintext from user input is then encrypted with the public key and decrypted with the private key.

def isPrimeNumber(number):
    if (number==1):
        return False
    elif (number==2):
        return True;
    else:
        for x in range(2,number):
            if(number % x==0):
                return False
        return True   

def gcd(phiOfMod, e):
    if e <= 1 or e >= phiOfMod:
        return -1

    while e != 0:
        phiOfMod, e = e, phiOfMod % e
    return phiOfMod

def isCoprimeNumber(phiOfMod, e):
    return gcd(phiOfMod, e) == 1

def modInverse(e, mod):
    for d in range(1, mod):
        if (e * d) % mod == 1:
            return d
    return -1

def encrypt(plaintext, e, mod):
    return pow(plaintext, e, mod)    

def decrypt(ciphertext, d, mod):
    return pow(ciphertext, d, mod)

def main(): # main function
    prime1 = 0
    prime2 = 0
    e = 0
    d = 0
    plaintext = 0
    ciphertext = 0
    isPrime = False
    isCoprime = False

    # Enter in number 1 until it is prime
    while isPrime == False:
        prime1 = int(input("Enter prime number 1: "))
        isPrime = isPrimeNumber(prime1)

    # Enter in number 2 until it is prime
    isPrime = False;
    while isPrime == False or prime1 == prime2:
        prime2 = int(input("Enter prime number 2: "))
        isPrime = isPrimeNumber(prime2)
    
    # Calculate mod and phi of mod
    mod = prime1 * prime2
    phiOfMod = (prime1 - 1) * (prime2 - 1)

    # Enter in encryption key (public key) until it is coprime of phi of mod
    while isCoprime == False:
        e = int(input("Enter exponent: "))
        isCoprime = isCoprimeNumber(phiOfMod, e)

    # Calculate multiplicative inverse of e mod phiOfMod (private key)
    d = modInverse(e, phiOfMod)

    # Enter in integer to use as plaintext
    while plaintext <= 0 or plaintext >= mod:
        plaintext = int(input("Enter plaintext integer: "));

    # Print plaintext integer
    print("Plaintext (Before Encryption): " + str(plaintext))

    # Encrypt plaintext with public key and print result
    ciphertext = encrypt(plaintext, e, mod)
    print("Ciphertext (After Encryption): " + str(ciphertext))

    # Decrypt ciphertext with private key and print result
    plaintext = decrypt(ciphertext, d, mod)
    print("Plaintext (After Decryption): " + str(plaintext))

if __name__ == "__main__":
    main()
       
    
 

