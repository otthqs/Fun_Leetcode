# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        # 为了使得每一个intervals都被考虑到，没有意外的情况发生，可以先将interval按照起点的大小，从小到大进行排序

        intervals.sort(key = lambda x: x.start)

        # 初始化一个用于存放结果的list
        res = []

        # 对每一个unit进行合并，如果res空，则填一个进去，如果res不空把最后的一个取出来进行比较
        for unit in intervals:
            if not res:
                res.append(unit)

            pre = res[-1]

            if unit.start <= pre.end:
                pre.end = max(pre.end,unit.end)

            else:
                res.append(unit)

        return res
