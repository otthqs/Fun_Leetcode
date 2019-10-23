class Solution:
    def canMeasureWater(self, x, y, z):
        """
        :type x: int
        :type y: int
        :type z: int
        :rtype: bool
        """

        #其实就是找最大公约数的问题


        if x + y < z:
            return False

        if x+y == z:
            return True

        if z==0:
            return True

        if x==z or y==z:
            return True

        if x==0 or y==0:
            return False

        if x>y:
            x,y = y,x

        res = 1

        def gcd(x,y):
            if x<y:
                x,y = y,x
                while x % y != 0:
                    x,y = y, x%y
                return y

        res = gcd(x,y)


        if z%res==0:
            return True

        return False
