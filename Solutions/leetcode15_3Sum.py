class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # 三个数字相加等于目标数字，Brute force需要经过三重循环
        # 利用sort将数组进行排序后，用两个指针分别从头和尾开始运行将时间复杂度降到 n的平方

        res = []

        nums.sort()

        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue


            j = i+1
            k = len(nums) - 1
            while j < k:
                # 因为要对他们的和进行判断，用一个变量来存储这样的和，不然同样的计算要进行三次，浪费时间
                s = nums[i] + nums[j] + nums[k]
                if s == 0:
                    res.append([nums[i],nums[j],nums[k]])
                    j += 1
                    k -= 1
                    while j < k:
                        # 确保第二大的数和最大的数都与原来的答案不同，避免重复答案的出现
                        if nums[j] == nums[j-1]:
                            j += 1
                        else:break

                    while j < k:
                        if nums[k]  == nums[k+1]:
                            k -= 1

                        else:
                            break


                if s > 0:
                    k -= 1

                if s < 0:
                    j += 1

        return res
