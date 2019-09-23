class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        # 三种颜色的排序，可以用3个指针来完成
        # 第一个指针进行遍历，第二个指之前全是0，第三个指针之后全是2
        # 当第一个指针遇上第三个指针的时候，结束循环


        #三个需要注意的点：
        #当 h 指针 +1 时，i 指针也需要 +1
        #循环终止条件为 i<=t
        #当每次 i 指针更新后，进入下一次循环

        h = i = 0
        t = len(nums) - 1

        # i <= t进入循环，因为每次指针变动后，要进行判断当前位置是否合法
        while i <= t:
            if nums[i] == 0:
                #指针 i 扫过的都是1，指针i,j之间的都是1,交换了0,1后，两个指针同时变动
                #同时也是满足 i 指针位置要大于等于head指针

                # 注意每次 i 动，进入下一次循环(如果不写成continue的形式的话，需要将循环体结构部分改为if,elif,elif的形式，确保每次变化后进入下一个循环)
                nums[i],nums[h] = nums[h],nums[i]
                h += 1
                i += 1
                continue

                # 注意每次i动，进入下一次循环
            if nums[i] == 1:
                i += 1
                continue

            # 只变动 t 指针
            if nums[i] == 2:
                nums[i],nums[t] = nums[t],nums[i]
                t -= 1
