import collections
class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:

        #用来存取同一个人名的不同的操作，之后在进行判断这些操作是否invalid
        refDict = collections.defaultdict(list)
        invalid = set()
        for trans in transactions:
            trans = trans.split(',')
            if int(trans[2]) > 1000:
                invalid.add(','.join(trans))
            refDict[trans[0]].append(trans)


        for k,v in refDict.items():
            v.sort(key = lambda x: int(x[1]))
            if k == 'bob':
                print(v)
            for i in range(len(v)-1):
                refNode = v[i]
                for j in range(i+1,len(v)):
                    each = v[j]
                    if int(each[1]) - int(refNode[1]) <= 60:
                        if each[-1] != refNode[-1]:
                            invalid.add(','.join(refNode))
                            invalid.add(','.join(each))
                    else:
                        break

        return invalid
