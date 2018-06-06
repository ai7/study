# https://leetcode.com/explore/interview/card/top-interview-questions-medium/113/math/821/
# https://leetcode.com/problems/fraction-to-recurring-decimal/

# Fraction to Recurring Decimal
#
# Given two integers representing the numerator and denominator of a
# fraction, return the fraction in string format.
#
# If the fractional part is repeating, enclose the repeating part in
# parentheses.

import math
import unittest


class Solution:

    # Note: do long division, track reminder and detect repeat.
    #
    # The long division is not difficult to get right. However
    # tracking the reminder and detect a repeat and produce the
    # correct loop in parenthesis took some time to get all the corner
    # cases correct.
    #
    # start with x in history set, everytime we get a new reminder,
    # add to set. But, we also need to add intermediate x value before
    # it exceeds y into the set. (ie, x * 10 is still smaller than y).
    # So, not only the initial reminder value, but also any
    # intemediate values (the final value before division will
    # obviously be bigger than y so no need to add it to set).
    #
    # we store with each reminder the position in the answer array
    # where the next divided value is calculated. (basically the
    # position to the stuff on top [after decimal point] of the manual
    # long divide approach).
    #
    # An interesting trick to handle signs
    #   sign = '-' if (x > 0) ^ (y > 0) else ''
    
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        return self.my_decimal(numerator, denominator)

    # 37 / 37 test cases passed.
    # Status: Accepted (after 8 submissions!)
    # Runtime: 36 ms (beats 99.18% of py3)
    def my_decimal(self, x, y):

        # decimal representation of x/y assume both positive
        def calc_decimal(x, y):

            res = ''
            if y == 1:  # divide by 1, done
                return str(x)
            if x == y:  # x/x, done
                return '1'
            elif x > y:  # top is bigger, figure out whole part first
                res = str(x // y)
                x = x % y  # reminder
            else:  # x < y
                res = '0'

            if x == 0:  # if no reminder, done
                return res

            g = math.gcd(x, y)  # reduce fraction part first
            if g > 1:
                x, y = x // g, y // g

            # now work on the fraction part, x < y and already simplified
            res += '.'
            ans = []
            r_hist = {x: 0}  # track the reminders we've seen

            r = x  # start with first decimal
            while r:
                r *= 10
                if r in r_hist:  # if seen before, done
                    break
                if r == y:  # if same, done
                    ans.append(1)
                    r = 0
                    break
                elif r < y:  # if still not enough, do next loop
                    ans.append(0)   # push 0 to result
                    r_hist[r] = len(ans)  # add new r to history
                else:  # r > y, do the divide
                    w = r // y  # whole part
                    ans.append(w)  # add digit to answer
                    r_hist[r] = len(ans)  # remember this reminder
                    r = r % y  # calc reminder for next round

            if r:  # must be loop, enclose in ()
                idx = r_hist[r]
                res += ''.join(map(str, ans[:idx-1]))  # result before repeat, if any
                res += '(' + ''.join(map(str, ans[idx-1:])) + ')'  # repeat section enclosed in ()
            else:  # no reminder
                res += ''.join(map(str, ans))

            return res

        if x == 0:  # special case it
            return '0'  # no need to return -0 if negative

        # handle positive/negative stuff
        sign = '-' if (x > 0) ^ (y > 0) else ''
        return sign + calc_decimal(abs(x), abs(y))


class TestFraction(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test_no_reminder(self):
        self.assertEqual(self.sol.fractionToDecimal(1, 1), '1')
        self.assertEqual(self.sol.fractionToDecimal(2, 1), '2')
        self.assertEqual(self.sol.fractionToDecimal(100, 2), '50')
        self.assertEqual(self.sol.fractionToDecimal(3, 3), '1')
        self.assertEqual(self.sol.fractionToDecimal(9, 3), '3')

    def test_no_repeat(self):
        self.assertEqual(self.sol.fractionToDecimal(1, 2), '0.5')
        self.assertEqual(self.sol.fractionToDecimal(12, 24), '0.5')
        self.assertEqual(self.sol.fractionToDecimal(99, 4), '24.75')
        self.assertEqual(self.sol.fractionToDecimal(99, 5), '19.8')
        self.assertEqual(self.sol.fractionToDecimal(99, 6), '16.5')

    def test_repeat(self):
        self.assertEqual(self.sol.fractionToDecimal(1, 6), '0.1(6)')
        self.assertEqual(self.sol.fractionToDecimal(1, 7), '0.(142857)')
        self.assertEqual(self.sol.fractionToDecimal(2, 7), '0.(285714)')
        self.assertEqual(self.sol.fractionToDecimal(1, 90), '0.0(1)')
        self.assertEqual(self.sol.fractionToDecimal(4, 333), '0.(012)')
        self.assertEqual(self.sol.fractionToDecimal(32, 337), '0.(094955489614243323442136498516320474777448071216617210682492581602373887240356083086053412462908011869436201780415430267062314540059347181008902077151335311572700296735905044510385756676557863501483679525222551928783382789317507418397626112759643916913946587537091988130563798219584569732937685459940652818991097922848664688427299703264)')

    def test_negative(self):
        self.assertEqual(self.sol.fractionToDecimal(-50, 8), '-6.25')
        self.assertEqual(self.sol.fractionToDecimal(-50, -8), '6.25')
        self.assertEqual(self.sol.fractionToDecimal(50, -8), '-6.25')
        self.assertEqual(self.sol.fractionToDecimal(-1, 7), '-0.(142857)')
        self.assertEqual(self.sol.fractionToDecimal(0, -5), '0')


if __name__ == '__main__':
    unittest.main()
