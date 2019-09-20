import collections
class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        # 首先用一个hashtable统计每一个数的频率,并记录最大的频率
        refdic = {}
        maxfreq = 0
        for num in nums:
            refdic[num] = refdic.get(num,0) + 1
            maxfreq = max(maxfreq, refdic[num])

        # 按照每个value的频率作为key，将数字作为value放入我们的bucket中，进行桶排序
        bucket = collections.defaultdict(list)
        for v,l in refdic.items():
            bucket[l].append(v)


        res = []

        for i in range(maxfreq,0,-1):
            res += bucket[i]
            if len(res) == k:
                return res

        # We should never get here
        return None


class Solution:
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """


        # 建立字典统计频率
        # 将频率进行排序后取出结果


        dct = {}
        lst = []
        returnlst = []

        for i in nums:
            dct[i] = dct.get(i,0)+1

        for key,value in list(dct.items()):
            lst.append((value,key))

        lst.sort(reverse=True)

#         for value,key in lst[:k]:
#             returnlst.append(key)

        return [unit[1] for unit in lst[:k]]
