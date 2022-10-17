
def SieveOfEratosthenes(num):
    prime = [True for i in range(num+1)]
    print(prime)
# boolean array
    p = 2
    while (p * p <= num):

        # If prime[p] is not
        # changed, then it is a prime
        if (prime[p] == True):

            # Updating all multiples of p
            for i in range(p * p, num+1, p):
                prime[i] = False
        p += 1

    # Print all prime numbers
    for p in range(2, num+1):
        if prime[p]:
            print(f'p: {p}: bin: {bin(p)}')


FIRST_PRIME = 2


def n_th_prime(n):
    primes = [FIRST_PRIME]
    n_th_prime = FIRST_PRIME
    while (len(primes) < n):
        n_th_prime += 1
        isDivisibleByPrime = False
        for p in primes:
            if n_th_prime % p == 0:
                isDivisibleByPrime = True
        if not isDivisibleByPrime:
            isDivisibleByPrime = False
            primes.append(n_th_prime)
    return n_th_prime


def find_prime_larger_than_n(n):
    prime_1 = 2
    prime_2 = 3
    result_prime = prime_1
    while (result_prime < n):
        result_prime = prime_1*prime_2+1
        # prime_1 = prime_2
        prime_2 = result_prime

    return result_prime


print(find_prime_larger_than_n(10**13))
