class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: List
        """

        # 将两个listnode提取出来 在进行相加
        str1 = ""
        str2 = ""

        while l1:
            str1 += str(l1.val)
            l1 = l1.next


        while l2:
            str2 += str(l2.val)
            l2 = l2.next


        str1 = str1[::-1]
        str2 = str2[::-1]

        temp_sum = int(str1)+int(str2)

        temp_str = str(temp_sum)

        temp_str = temp_str[::-1]

        res = []

        for unit in temp_str:
            res.append(int(unit))

        return res
