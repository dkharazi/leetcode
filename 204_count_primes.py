# 204. Count Primes
#
# Count the number of prime numbers less than a non-negative number, n.


class Solution(object):
    #  Time Limit Exceeded
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        count = 0
        for i in range(2, n):
            if self.isPrime(i):
                count += 1
        return count

    def isPrime(self, n):
        import math
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return False
        return True

    # https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
    # TLE
    def countPrimes(self, n):
        if n <= 2:
            return 0

        P = [_ for _ in range(2, n)]
        p = 0
        while True:
            for i in P[p + 1:]:
                if i % P[p] == 0:
                    P.remove(i)
            if P[p] ** 2 >= P[-1]:
                break
            p += 1
        return len(P)

    # http://bookshadow.com/weblog/2015/04/27/leetcode-count-primes/
    def countPrimes(self, n):
        isPrime = [True] * max(n, 2)
        isPrime[0], isPrime[1] = False, False
        x = 2
        while x * x < n:
            if isPrime[x]:
                # only consider starting from x**2
                # the left has been marked by smaller than x
                p = x * x
                while p < n:
                    isPrime[p] = False
                    p += x
            x += 1
        return sum(isPrime)

if __name__ == '__main__':
    print Solution().countPrimes(30)
