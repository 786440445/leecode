class Graph:
    def __init__(self, arcs=[]):
        self.vexs = [] #点集合
        self.arcs = arcs #矩阵路径

    def creategrapg(self):
        self.vexs = input().split()
        for i in range(len(self.vexs)):
            self.arcs.append([float('inf') if int(v) == 0 else int(v) for v in input().split()])

    def ShortestPath_DIJ(self, v):
        # 迪杰斯特拉算法
        # 第几个点为起始点
        v0 = self.vexs.index(v)
        n = len(self.vexs)
        S = [False] * n
        S[v0] = True
        D = self.arcs[v0].copy()
        Path = [-1] * n

        for i in range(n):
            if D[i] < float('inf'):
                Path[i] = v0

        # 到本身为0
        D[v0] = 0
        for i in range(1, n):
            min_ = float('inf')
            for w in range(n):
                if not S[w] and D[w] < min_:
                    v_ = w
                    min_ = D[w]
            S[v_] = True
            for w in range(n):
                if not S[w] and (D[v_] + self.arcs[v_][w] < D[w]):
                    D[w] = D[v_] + self.arcs[v_][w]
                    Path[w] = v_


        print(f'从{v}到各顶点的最短路径为:')
        # 算法到此其实已经结束，下面我自己写的用来展示路径的部分
        for ind, val in enumerate(Path):
            if ind == v0:
                continue
            if val == -1:
                print(f'{self.vexs[ind]}:不可到达')
                continue
            path_ = [self.vexs[ind]]
            while val > 0:
                path_.append(self.vexs[val])
                val = Path[val]
            # path_.append(v)
            print(self.vexs[ind] + ':' + '->'.join(path_[::-1]))

# mygraph = Graph()
# mygraph.creategrapg()
# mygraph.ShortestPath_DIJ(mygraph.vexs[1])


V = 7
used = [False for _ in range(V)]
distance = [float('inf') for _ in range(V)]
cost = [[float('inf') for _ in range(V)] for _ in range(V)]


def dijkstra(s):
    distance[s] = 0
    while True:
        v = -1
        for u in range(V):
            if not used[u] and (v == -1 or distance[u] < distance[v]):
                v = u
        if v == -1:
            break

        used[v] = True
        # 更新图路径
        for u in range(V):
            if cost[v][u] != float('inf'):
                distance[u] = min(distance[u], distance[v] + cost[v][u])
