"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        #用一个refDict来记录哪些node已经建立好了，哪些没有建立好，key为这个Node，value为我们想要的东西；用dfs的方法来解决
        refDict = {}
        def dfs(node):
            if node not in refDict:
                copy = Node(val = node.val ,neighbors = None)
                refDict[node] = copy
                copy.neighbors = [dfs(n) for n in node.neighbors]

            return refDict[node]

        return dfs(node)
         
