class Solution:
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        #因为输入的K值总是有效的，我们可以先忽略掉edge case的情况

        #利用快速查询的方法进行搜索查找





        # 选取一个pivot
        pivot = nums[0]

        left = []

        right = [pivot]

        # 对数组进行分组
        for i in range(1,len(nums)):
            if nums[i] >= pivot:
                right.append(nums[i])

            else:
                left.append(nums[i])


        if len(right) == k:
            return right[0]

        # 如果比pivot多的数目比k多，去掉pivot进行循环
        elif len(right) > k:
            right.pop(0)
            return self.findKthLargest(right,k)

        # 如果比pivot多的数目比k少，从剩下的数组中，找第k-len(right)大的数字即为所求
        elif len(right) < k:
            return self.findKthLargest(left,k-len(right))
