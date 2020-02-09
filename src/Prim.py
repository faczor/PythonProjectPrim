from src.Reader import Reader


class Prim:

    def __init__(self, graph):
        self.__graph = graph

    def prep_link_cost(self, neigh):
        tmp = []
        for i in range(graph.vertex_size):
            tmp.append([0] * graph.vertex_size)
        for i in range(graph.vertex_size):
            for x in range(graph.vertex_size):
                if neigh[i][x] == 0:
                    tmp[i][x] = 99999
                else:
                    tmp[i][x] = neigh[i][x]
        return tmp

    def main_alg(self):
        for i in range(graph.vertex_size):
            for x in range(graph.vertex_size):
                print(graph.neighbours[i][x], end=", ")
            print()
        reached, predNode, min_cost = [], [], 0
        link_cost = self.prep_link_cost(graph.neighbours)
        for i in range(graph.vertex_size):
            reached.append(False)
            predNode.append(99999)
        reached[0] = True
        predNode[0] = 0
        self.print_reach_set(reached)
        for k in range(graph.vertex_size - 1):
            x, y = 0, 0
            for i in range(graph.vertex_size):
                for j in range(graph.vertex_size):
                    if reached[i] and not reached[j] and link_cost[i][j] < link_cost[x][y]:
                        x, y = i, j
            print("Min cost edge: (", x, ", ", y, ")", "cost = ", link_cost[x][y])
            min_cost += link_cost[x][y]
            predNode[y], reached[y] = x, True
            self.print_reach_set(reached)
        print("Minimal Spanning Tree Weight = ", min_cost)

    def print_reach_set(self, reached):
        print("ReachSet:", end=" ")
        for i in range(graph.vertex_size):
            if reached[i]:
                print(i, " ", end="")
        print()

    @property
    def graph(self):
        return self.__graph


file_name = "example1.txt"
graph = Reader(file_name).graph
prim = Prim(graph)
prim.main_alg()
