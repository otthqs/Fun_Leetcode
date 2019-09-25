class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        refSet = set()
        for c in nums:
            if c in refSet:
                return True

            refSet.add(c)

        return False
