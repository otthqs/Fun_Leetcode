class Solution:
    def validIPAddress(self, IP):
        """
        :type IP: str
        :rtype: str
        """
        set1 = ("0","1","2","3","4","5","6","7","8","9","A","a","B","b","C","c","D","d","E","e","f","F")

        def isIPV6(IP):
            if len(IP.split(":")) != 8:
                return False

            else:
                IP = IP.split(":")
                for each in IP:
                    if len(each) >=5 or len(each)<1:
                        return False
                    else:
                        for j in each:
                            if j not in set1:
                                return False

            return "IPv6"

        def isIPV4(IP):
            if len(IP.split(".")) !=4:
                return False

            else:
                IP = IP.split(".")
                for each in IP:
                    try:
                        int(each)
                    except:
                        return False

                    if int(each)<0 or int(each)>255 or len(str(int(each))) != len(each):
                        return False


            return "IPv4"

        res1 = isIPV4(IP)
        res2 = isIPV6(IP)

        if res1:
            return res1

        elif res2:
            return res2

        else:
            return "Neither"
