class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if not digits:
            return []
        # 用list comprehension 不断更新 list 最终得到正确的结论
        # 先创造一个ref_list 来存每个数字能对应到的字母数目

        ref = [[],[],["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]

        res = [""]

        for unit in digits:
            res = [m + n for m in res for n in ref[int(unit)]]

        return res
