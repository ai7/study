// https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/648/
// https://leetcode.com/problems/reverse-bits/description/

// Reverse Bits
//
// Reverse bits of a given 32 bits unsigned integer.

// this is not flip the bits, but rather, reverse the bits (like reverse string)

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>


// 600 / 600 test cases passed.
// Runtime: 12 ms
// only beats 20.73% of C submission
uint32_t reverseBits(uint32_t n) {

    // this is what I came up with. Sort of based on the short-circuit
    // hamming weight calculation.
    
    uint32_t v = 0;
    uint32_t mask = (1 << 31);  // set MSB to 1
    while (n) {  // while n have some bits on
        if (n & 1) {  // if LSB bit is on
            v |= mask;
        }
        n >>= 1;
        mask >>= 1;
    }
    return v;
}


// 600 / 600 test cases passed.
// Runtime: 4 ms
// beats 86.59% of C submission
//
uint32_t reverseBits2(uint32_t n) {

    // From forum post. It's interesting that this is 3 times faster
    // than above. not obvious from the code. Perhaps the compiler can
    // optimize this better?

    uint32_t v = 0;
    for (int i = 0; i < 32; i++, n >>= 1) {
        v <<= 1;
        v |= (n & 1);  // set v's LSB to on if n's LSB is on
    }
    return v;
}


int main(int argc, char *argv[], char *env[]) {

    if (argc < 2) {
        printf("Usage: %s <n>\n", argv[0]);
        return 1;
    }

    uint32_t n = atoi(argv[1]);
    // uint32_t v = reverseBits(n);
    uint32_t v = reverseBits2(n);

    printf("%u: %u\n", n, v);

    return 0;
}
