# https://leetcode.com/explore/interview/card/top-interview-questions-medium/114/others/826/
# https://leetcode.com/problems/task-scheduler/description/

# Task Scheduler
#
# Given a char array representing tasks CPU need to do. It contains
# capital letters A to Z where different letters represent different
# tasks.Tasks could be done without original order. Each task could be
# done in one interval. For each interval, CPU could finish one task
# or just be idle.
#
# However, there is a non-negative cooling interval n that means
# between two same tasks, there must be at least n intervals that CPU
# are doing different tasks or just be idle.
#
# You need to return the least number of intervals the CPU will take
# to finish all the given tasks.

# Question is confusing, this is essentially how to place a set of
# tokens in an array such that same items are separated by at least n
# elements in between.

import collections
import heapq
import unittest


class SlidingWindow:

    def __init__(self, n):
        self.q = collections.deque()
        self.n = n

    # add item to queue, pop oldest item if applicable
    def add(self, item):
        self.q.append(item)
        if len(self.q) > self.n:
            return self.q.popleft()

    # pop the oldest item from queue
    def pop(self):
        if self.q:
            return self.q.popleft()

    def has_work(self):
        for x in self.q:
            if x.name != 'idle' and x.n > 0:
                return True
        return False

    def __len__(self):
        return len(self.q)

    def __repr__(self):
        s = ', '.join([repr(x) for x in self.q])
        return 'SlidingWindow(%d) [%s]' % (self.n, s)


class Task:

    def __init__(self, name, n):
        self.name = name  # name, A, B, etc.
        self.n = n  # occurrences of this task

    def __repr__(self):
        return 'Task(%s, %d)' % (self.name, self.n)

    def schedule(self):  # schedule one instance of task
        self.n -= 1

    def has_remain(self):  # any more instance for this task?
        return self.n > 0

    # invert comparison for storing in max heap
    def __lt__(self, other):
        return self.n > other.n

    def __eq__(self,other):
        return self.n == other.n


class Solution:

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        return self.calc_schedule(tasks, n)

    # Note: schedule task with highest count
    #
    # Came up with this myself. Always try to schedule task with the
    # highest count.
    #
    # To do this, we utialize a max heap, which always returns tasks
    # with the highest count. We also use a sliding window, and move
    # objects between the max_heap and sliding window as appropriate.
    #
    # when we pop item from sliding window, we drop it if count is 0.
    # (we do want to add 0-count item to sliding window after
    # scheduling/use it so it will nicely squeeze out other items in
    # the sliding window).

    # There apparently is a solution based on scheduling the most
    # frequent jobs first (with appropriate spacing for idle time),
    # then the next most frequent job one, etc.. But have a way to
    # calculate the length of the array without physically
    # constructing the array. Intersting, but hard to understand damn
    # it.

    # 64 / 64 test cases passed.
    # Status: Accepted (on 1st try! ;)
    # Runtime: 2564 ms (beats 4.17% of py3)
    def calc_schedule(self, tasks, n):

        if not tasks:  # if no task to schedule
            return 0
        if n < 1:  # if no restriction
            return len(tasks)  # then just the length of tasks

        counter = collections.Counter(tasks)  # get task and their counts
        idle = Task('idle', 0)  # dummy task for idle work

        # add tasks to a max heap
        max_heap = []
        for c in counter:
            heapq.heappush(max_heap, Task(c, counter[c]))

        sw = SlidingWindow(n)  # create a sliding window of size n

        schedule = []  # actual schedule for debugging
        while max_heap or sw.has_work():
            if max_heap:  # if have item in max heap, use it
                x = heapq.heappop(max_heap)
                x.schedule()  # decrement task
                schedule.append(x.name)
                y = sw.add(x)  # add task to sliding window
                if y and y.name != 'idle' and y.has_remain():
                    heapq.heappush(max_heap, y)    # add any task from sliding window back to heap
            else:  # sliding window has item, but max_heap is exhausted
                schedule.append(idle.name)
                y = sw.add(idle)
                if y and y.name != 'idle' and y.has_remain():
                    heapq.heappush(max_heap, y)

        return len(schedule)


class TestSchedule(unittest.TestCase):

    def setUp(self):
        self.sol = Solution()

    def test1(self):
        A = ["A","A","A","B","B","B"]
        self.assertEqual(self.sol.leastInterval(A, 2), 8)


if __name__ == '__main__':
    unittest.main()
