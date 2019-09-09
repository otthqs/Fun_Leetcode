class Solution:
    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """

        # 这所有人里面，最矮的人是和其他人没关系的
        # 最矮的人里面，k,v in person, v最大的就是这个人应该在的位置

        res = []

        people.sort(key = lambda x:[x[0],-x[1]], reverse = True)

        # 这样排好之后，最矮的人中k最大的在最后，应该最后插入
        # 迭代下去，最先插入第一个，接着插入其他即可

        for person in people:
            res.insert(person[1],person)

        return res
