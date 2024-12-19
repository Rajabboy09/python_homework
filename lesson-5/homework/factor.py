def factors(n):
    for i in range(1,n+1):
        if n%i==0:
            print(f"{i} is factor of {n}")
n = int(input("Enter your number: "))
factors(n)