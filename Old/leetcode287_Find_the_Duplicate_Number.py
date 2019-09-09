class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # 要求空间space是 O(1), 不能改变原函数，所以不能遍历函数，看有无重复，也不能用set进行排除

        # 因为一共有 n+1 个数字，数字从只能从 1-n,所以 nums[i]作为index一直索引的话，index = nums[nums[index]]，可以无限重复下去，这样的话，我们就一定有一个环

        # 因为 0 不在这 n+1 个数字中，所以如果从 nums[0]开始索引的话，一定会在某个时刻进入环，而进入环的开始就是重复的数字。

        slow = nums[nums[0]]

        fast = nums[nums[nums[0]]]

        while slow != fast:
            slow = nums[slow]
            fast = nums[nums[fast]]


        slow = nums[0]

        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
