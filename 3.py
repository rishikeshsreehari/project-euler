'''
Problem 3:
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?

'''


n = 600851475143

def prime_factor(n):
    factors = []
    while n % 2 == 0:
        factors = factors.append(2)
        n = n//2

    for i in range(3, int(n**0.5)+1, 2):
        while n % i == 0:
            factors.append(i)
            n = n // i

    if n > 2:
        factors.append(n)

    return factors


factors = prime_factor(n)
print(max(factors))


     


