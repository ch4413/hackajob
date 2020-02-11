def find_primes(n):
    """
    Finds list of primes up to and includes n
    Args:
        n (int) upper bound
    Returns:
        list_primes (list) list of primes
    """
    list_primes = []
    for num in range(0, n + 1):
        # all prime numbers are greater than 1
        if num > 1:
            for i in range(2, num):
                if (num % i) == 0:
                    break
            else:
                list_primes.extend([num])
    return list_primes


def check_factors(n, list_of_factors):
    """
    Checks list_of_factors against n. Returns True if
    there is a pair.
    Args:
        n (int) value to check for factors
        list_of_factors (list) list of integers
    Returns:
        has_factors (bool) Flag True if factor pair found
    """
    has_factors = False
    for i in list_of_factors:
        a = (n / i)
        if a.is_integer():
            if (a in list_of_factors) & (n == (a * i)):
                has_factors = True
                return has_factors  # (a, i)
        else:
            pass
    return has_factors


class Solution:

    def run(self, number):
        list_primes = find_primes(number)
        is_semiprime = check_factors(number, list_primes)
        return is_semiprime
