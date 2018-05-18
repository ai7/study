# https://leetcode.com/explore/interview/card/top-interview-questions-easy/98/design/562/
# https://leetcode.com/problems/min-stack/description/

# Min Stack
#
# Design a stack that supports push, pop, top, and retrieving the
# minimum element in constant time.

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()


class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.min_s = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stack.append(x)  # always add to stack
        if self.min_s:
            if x <= self.min_s[-1]:  # if not greater add to min stack
                self.min_s.append(x)
        else:
            self.min_s.append(x)

    def pop(self):
        """
        :rtype: void
        """
        v = self.stack.pop()
        if v == self.min_s[-1]:  # if same as min stack, pop it
            self.min_s.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return self.min_s[-1]

    # 18 / 18 test cases passed.
    # beats 100% of py3, yeah!
