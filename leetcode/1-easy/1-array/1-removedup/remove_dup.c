
// https://leetcode.com/submissions/detail/149715599/
// 161 / 161 test cases passed.

int removeDuplicates(int* nums, int numsSize) {
    int i = 0;
    int j = 0;
    while (j < numsSize) {
        nums[i] = nums[j];
        while (j < numsSize && nums[j] == nums[j+1]) {
            j++;
        }
        i++;
        j++;
    }
    return i;
}
