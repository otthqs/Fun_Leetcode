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
