def is_prime(n):
    prime = True
    for i in range(2,n):
        if n%i == 0:
            prime=False
    return prime

numm = int(input("Enter your number: "))
print(is_prime(numm))