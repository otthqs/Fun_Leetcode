class Solution:
    def longestPalindrome(self, s: str) -> int:
        res, ref_set = 0, set()
        for unit in s:
            if unit not in ref_set: ref_set.add(unit)
            else:
                res += 1
                ref_set.remove(unit)

        return 2 * res if not ref_set else 2 * res + 1
