class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        #一个小数点一个小数点的比
        i, j = 0, 0
        while i < len(version1) or j < len(version2):
            v,k = 0, 0
            while i < len(version1) and version1[i] != '.':
                v = 10 * v + int(version1[i])
                i += 1

            while j < len(version2) and version2[j] != '.':
                k = 10 * k + int(version2[j])
                j += 1

            if v != k:
                return 1 if v > k else -1

            i += 1
            j += 1

        return 0
