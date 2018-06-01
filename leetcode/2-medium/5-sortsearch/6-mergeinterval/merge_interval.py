# https://leetcode.com/explore/interview/card/top-interview-questions-medium/110/sorting-and-searching/803/
# https://leetcode.com/problems/merge-intervals/description/

# Merge Intervals
#
# Given a collection of intervals, merge all overlapping intervals.


# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        return self.merge2(intervals)

    # Note: sort interval, grow or add successive intervals.
    #
    # first sort interval by starting point.
    # then for each interval b in input A[1:]
    #   grow last interval if b overlap with last one
    #   add b as new interval if does not overlap.
    
    # my solution, after optimization
    # still only beat 54.47%, hmmmmm
    def merge2(self, A):
        if not A:  # return if no data
            return []
        A.sort(key=lambda x: x.start)  # sort by start time, in place
        retval = [A[0]]  # now go through array
        for b in A[1:]:
            a = retval[-1]  # last element of retval
            # if a.end < b.start or b.end < a.start:  # test for overlap
            if a.end < b.start:  # test for overlap (no need to test 2nd case, since sorted)
                retval.append(b)  # no overlap, add b to return list
            else:  # overlap, extend end if necessary
                a.end = max(a.end, b.end)
        return retval

    # my function, used by merge1
    def union(self, a, b):
        """Return the union of the 2 intervals, or None if they don't intersect"""

        if a.end < b.start or b.end < a.start:  # if a before b, or b before a, false
            return None

        # make x the first interval
        x = a if a.start <= b.start else b
        y = b if a.start <= b.start else b

        # assert a.start <= b.start

        if b.end <= a.end:  # b is entirely in a
            return Interval(a.start, a.end)
        else:
            return Interval(a.start, b.end)

    # 169 / 169 test cases passed.
    # Runtime: 80 ms (40.88%)
    def merge1(self, A):

        if not A:
            return []

        # sort array of obj by their start/end time
        A = sorted(A, key=lambda x: (x.start, x.end))

        retval = [A[0]]
        for v in A[1:]:
            u = self.union(retval[-1], v)  # returns a new obj, probably slow
            if u:  # if they meet, replace last element with union
                retval[-1] = u
            else:  # otherwise, add new element to retval
                retval.append(v)

        return retval

    # for illustration purpose, not used below
    def overlap(self, a, b):
        """Test if interval a or b overlap"""
        if a.end < b.start or b.end < a.start:
            return False
        return True  # otherwise must overlap

    # from StefanPochmann
    # 68 ms (beats 92.45%)
    # I don't understand why this is significantly faster than 2 or 1 above...
    def merge3(self, A):
        out = []
        for i in sorted(A, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(i.end, out[-1].end)
            else:
                out.append(i)
        return out
