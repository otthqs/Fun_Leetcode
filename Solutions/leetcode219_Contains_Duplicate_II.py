# 利用字典来进行储存和计算
class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        refDict = {}

        for i,c in enumerate(nums):
            if c not in refDict:
                refDict[c] = i

            else:
                if i - refDict[c] <= k:
                    return True

                refDict[c] = i

        return False
