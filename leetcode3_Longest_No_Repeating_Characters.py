class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """


        # 用字典记录出现过的字母，key是这个字母，value是字母的序号
        d = {}
        # 需要记录不重复的substring从哪开始，到哪结束
        start = 0
        max_len = 0

        for i,c in enumerate(s):
            # 在一个新的substring开头后出现了重复的数字，更新最长substring，更新开头
            if c in d and d[c] >= start:
                max_len = max(max_len, i - start)
                start = d[c]+1
            d[c] = i

            # 每次遇到重复才更新，在最后没有重复的话也要进行更新
        max_len = max(max_len,len(s)-start)

        return max_len
