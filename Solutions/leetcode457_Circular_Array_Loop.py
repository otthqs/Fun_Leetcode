class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        #将题目看成一个有向的NodeList来看待，先写一个连接下一个index的函数，将nums构成环
        def nextNum(nums,i):
            return (i + nums[i]) % len(nums)

        for i,c in enumerate(nums):
            if c == 0:
                continue

            slow = fast = i
            while nums[nextNum(nums,slow)] * c > 0 and nums[nextNum(nums,fast)] * c > 0 and nums[nextNum(nums,nextNum(nums,fast))] * c > 0:
                slow = nextNum(nums,slow)
                fast = nextNum(nums,nextNum(nums,fast))
                if slow == fast:
                    if slow == nextNum(nums,slow):
                        break
                    return True


            #将走过的途径进行剪枝(速率从1380ms - 44ms)：
            slow = i
            while nums[slow] * c > 0:
                temp = nextNum(nums,slow)
                nums[slow] = 0
                slow = temp


        return False

        
