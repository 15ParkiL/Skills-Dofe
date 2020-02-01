def get_primes(n): 
    """
    Find all prime numbers between 0 and n
    Args:
        n (int): The input number to find primes up to.
    """
    primes = [True] * (n / 2)
    for i in range(int((n / 2 - 1) / 2) >> 1):
        for j in range((i * (i + 3) << 1) + 3, n / 2, (i << 1) + 3): 
            primes[j] = False
    return [2] + [((i << 1) + 3) for i in range(n / 2) if (primes[i])]

# test function

if __name__ == "__main__": #What does this do?
    print get_primes(input())