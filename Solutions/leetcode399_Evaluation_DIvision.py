import collections
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # 第一种方法，构造连通图，使用dfs搜索完成

        #构建连通图
        graph = collections.defaultdict(dict)
        for (x,y), z in zip(equations, values):
            graph[x][y] = z
            graph[y][x] = 1.0/z

        def dfs(x,y,visited):
            if x == y:
                return 1.0
            visited.add(x)

            for each in graph[x]:
                if each in visited:
                    continue

                res = dfs(each,y,visited)
                if res > 0:
                    return res * graph[x][each]

            return -1.0

        return [dfs(x,y,set()) if x in graph and y in graph else -1.0 for [x,y] in queries]



        # 第二种方法，用并查集的方法构建树来进行判断
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        def find(x):
            if x == root[x][0]:
                return root[x]

            else:
                t0,t1 = find(root[x][0])
                return [t0, t1 * root[x][1]]


        root = {}
        for (x,y), z in zip(equations, values):
            if x not in root and y not in root:
                root[x] = [y,z]
                root[y] = [y,1.0]
            elif x not in root:
                root[x] = [y,z]
            elif y not in root:
                root[y] = [x, 1.0 / z]

            else:
                rx, vx = find(x)
                ry, vy = find(y)
                root[rx] = [ry, z * vy / vx]

        res = []
        for (x,y) in queries:
            if x not in root or y not in root or find(x)[0] != find(y)[0]:
                res.append(-1.0)

            else:
                res.append(find(x)[1] / find(y)[1])

        return res
