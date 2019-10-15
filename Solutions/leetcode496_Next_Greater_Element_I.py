class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #用单调栈来解决问题，同时用一个Dict来记录nums2中单调栈的结果，在映射到nums1中去
        stack = []
        refDict = {}
        for i,c in enumerate(nums2):
            while stack and c > nums2[stack[-1]]:
                node = stack.pop()
                refDict[nums2[node]] = c

            stack.append(i)

        return [refDict[c] if c in refDict else -1 for c in nums1]
