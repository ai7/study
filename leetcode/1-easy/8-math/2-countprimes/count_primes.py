# https://leetcode.com/explore/interview/card/top-interview-questions-easy/102/math/744/
# https://leetcode.com/problems/count-primes/description/

# Count Primes
#
# Count the number of prime numbers less than a non-negative number, n.

import math
import unittest


class Solution:

    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # return self.count1(n)
        return self.count_sieve_of_eratosthenes(n)
        
    def is_prime(self, n):

        # some special case to speed it up
        if n == 2:
            return True
        if n % 2 == 0 or n <= 1:
            return False

        sqr = int(math.sqrt(n)) + 1

        return all(n % i for i in range(3, sqr, 2))  # python supports short circuit

    # 18 / 20 test cases passed.
    # time exceeded on 999983
    def count1(self, n):
        if n < 3:  # if n is 2 or below (meaning x less than 2), then no primes
            return 0

        count = 1
        for x in range(3, n, 2):
            if self.is_prime(x):
                count += 1

        return count

    # beats 37.77%, hmmmm
    # after inner loop start at k*k, and outer loop stop at sqrt(n)
    #   it is now 78.47%, hehe
    def count_sieve_of_eratosthenes(self, n):
        """Count the number of primes using special method"""

        if n < 3:  # if n is 2 or below (meaning x less than 2), then no primes
            return 0

        A = [True] * n  # create a table of size n, all set to true initially
        A[0] = A[1] = False  # base case, 0 and 1 are not primes

        # now go through and mark off as needed
        sqr = int(math.sqrt(n)) + 1

        for k in range(2, sqr):  # k from 2 to sqrt(n), in increment of 1

            if A[k]:  # if prime, mark off all multiple of this number

                # lets start with 2k (since k is already a prime)
                # better yet, start with k*k, since multiples of k before
                # that would've been cross off already
                for i in range(k*k, n, k):  # i from k*k to n, in increment of k
                    A[i] = False  # mark off number

        # now go through array and count the number of Trues
        p = sum(A)

        return p


class TestCount(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        self.assertEqual(self.sol.countPrimes(10), 4)


if __name__ == '__main__':
    unittest.main()
