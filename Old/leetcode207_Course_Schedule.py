class Solution:
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """

        # 这倒题给了我们课程的数目，我们可以设置一个ref的list，每次初始化为 [True]*numCourses
        # 接着对prerequisites中的list进行遍历，把所有有前提要求的course标记为False
        # 再次遍历prerequisites，注意目前ref里面仍然为True的course是指可以上的course，如果前提课程可以上，那么可以在prerequisites中去除这个course
        # 循环以上三个步骤，直到prerequisite为空或者循环一次后，一个多余的课都没上



        while prerequisites:

            ref = [True] * numCourses
            for course in prerequisites:
                ref[course[0]] = False

            count = 0

            for course in prerequisites:
                if ref[course[1]] == True:
                    prerequisites.remove(course)
                    count += 1

            if count == 0:
                break

        if prerequisites:
            return False

        else:
            return True
