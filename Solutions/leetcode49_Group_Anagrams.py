class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        #如果字母相同，那么属于同一组，因此将字母进行排序后就属于同一组
        d = {}

        for unit in strs:
            temp = "".join(sorted(unit))
            if temp in d:
                d[temp].append(unit)
            else:
                d[temp] = []
                d[temp].append(unit)

        return list(d.values())
            
