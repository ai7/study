// https://leetcode.com/explore/interview/card/top-interview-questions-easy/99/others/762/
// https://leetcode.com/problems/hamming-distance/description/

// Hamming Distance
//
// The Hamming distance between two integers is the number of positions
// at which the corresponding bits are different.
//
// Given two integers x and y, calculate the Hamming distance.

// 4ms
// beats 91.30% of C submission
int hammingDistance(int x, int y) {
    int count = 0;
    unsigned int n = (x ^ y);
    while (n) {
        count++;
        n &= (n - 1);  // clear right most bit that is on
    }
    return count;
}
