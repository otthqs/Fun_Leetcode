class Solution:
	def smallestRepunitDivByK(self, K: int) -> int:
		num=str(K)
		if num[-1] in {'2','4','5','6','8','0'}:
			return -1
		tem=1
		while tem%K!=0:
			tem=tem*10+1
		return len(str(tem))
        
