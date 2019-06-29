class Solution:
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """

        # 转换问题：
        # 如果n比任务数多的话即不能一直工作的话，需要有休息的话：
        # 转到最多的那个任务，如A出现了k次，那么每次做了A，在下次做A期间，就可以把所有任务做一遍
        # 则前（k-1）次循环，要做：(k-1)*(n+1)， 最后一次循环只需要做和A一样数目的最多的任务

        # 如果不需要休息的话，有几个任务就工作几天，第一种算法就少算了
        # 因此返回这两个数值的最大值即可

        # 需要找频率最大的工作数目，和最大频率出现了几次

        ref = {}

        count = 0

        for unit in tasks:
            ref[unit] = ref.get(unit,0) + 1
            if count < ref[unit]:
                count = ref[unit]

        fre = 0

        for v in ref.values():
            if v == count:
                fre += 1

        return max(len(tasks),(count-1)*(n+1)+fre)
