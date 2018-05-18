// https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/565/
// https://leetcode.com/problems/number-of-1-bits/description/

// Number of 1 Bits
//
// Write a function that takes an unsigned integer and returns the
// number of '1' bits it has (also known as the Hamming weight).

#include <stdio.h>
#include <stdint.h>


// 0ms
// from solution
// beats 100% of submission, wow
int hammingWeight2(uint32_t n) {
    int count = 0;
    while (n) {
        count++;
        n &= (n - 1);  // clear right most bit that is on
    }
    return count;
}


// 4ms
// 600 / 600 test cases passed.
// beats 86.43% of C submission
int hammingWeight(uint32_t n) {
    int count = 0;
    while (n) {
        if (n & 1) {  // if LSB is set
            count++;
        }
        n >>= 1;  // logical shift right
    }
    return count;
}


int main(int argc, char *argv[], char *env[]) {
    int v = hammingWeight(12);
    printf("%d: %d\n", 12, v);

    return 0;
}
