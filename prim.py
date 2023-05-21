import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

INPUT_PATH = "prim.txt"


def load_graph_from_file(path: str):
    """
    Returns a graph from a text file containing an adjacency matrix.
    Each line of the file contains a row of the adjacency matrix,
    with each entry separated by any number of spaces.
    """
    with open("prim.txt", "r") as f:
        graph = [
            [int(x) for x in line.split()]
            for line in f.readlines()
            if line.strip() != ""
        ]
    return graph


def plot_graph(graph: list):
    print(graph)
    G = nx.from_numpy_array(np.array(graph), parallel_edges=False)

    # Plot it
    nx.draw(G, with_labels=True)
    pos = nx.spring_layout(G)
    labels = nx.get_edge_attributes(G, "weight")

    print("pos:", pos)
    print("labels:", labels)

    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

    return G


def find_mst_prim(graph: list):
    """
    Returns the minimum spanning tree of the given graph using Prim's algorithm.
    """

    node_selected = [False for i in range(len(graph))]
    no_edge = 0
    node_selected[0] = True

    N = len(graph)
    minimum = float("-inf")
    a = 0
    b = 0

    mst = [[0 for i in range(N)] for j in range(N)]

    while no_edge < N - 1:
        minimum = float("inf")
        a = 0
        b = 0
        for m in range(N):
            if node_selected[m]:
                for n in range(N):
                    if (not node_selected[n]) and graph[m][n]:
                        # Not in selected edges and there is an edge
                        if minimum > graph[m][n]:
                            minimum = graph[m][n]
                            a = m
                            b = n
                            print(a, b)
        print(f"Edge {no_edge}: ({a}, {b}) cost: {minimum}")
        mst[a][b] = minimum

        node_selected[b] = True
        no_edge += 1

    return mst


def main():
    graph = load_graph_from_file(INPUT_PATH)
    print(graph)

    plot_graph(graph)
    mst = find_mst_prim(graph)
    plot_graph(mst)


if __name__ == "__main__":
    main()
