# sieve.py
# Sieve of Eratosthenes Algorithm
# By: Shahzeb Jadoon

def sieve(n):

    """Implements the sieve of Eratosthenes algorithm to find prime numbers

       Pre: n is an int > 1
       Post: Returns list of all prime numbers up till n (including n if it 
             is a prime number)
       """

    # Not an in-place algorithm
    a_lst = []

    # Create a list of size n
    for num in range(0, n+1):   
        a_lst.append(num)

    for p in range(2, int(sqrt(n))+1):

        if a_lst[p] != 0:
            j = p * p

            while j <= n:
                a_lst[j] = 0
                j = j + p
    
    prime_lst = []

    # First 2 elements are scrapped off
    for p in range (2, n):
        if a_lst[p] != 0:
            prime_lst.append(a_lst[p])

    return prime_lst


def main():
        """Generates list of primes using Sieve of Eratosthenes 
           up till user specified limit
        """

        print("This program uses the Sieve of Eratosthenes to calculate")
        print("Prime Numbers up to a specified integer provided by the user\n")

        num = int(input("Find primes until: "))
        lst = sieve(num)

        print("\nPrime numbers up to the integer", num, "are:\n")
        print(lst)


if __name__ == '__main__':
    from math import sqrt
    
    main()