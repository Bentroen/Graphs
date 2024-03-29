import matplotlib.pyplot as plt
import networkx as nx
import numpy as np

INPUT_PATH = "prim.txt"


AdjacencyMatrix = list[list[int]]


def load_graph_from_file(path: str):
    """
    Returns a graph from a text file containing an adjacency matrix.
    Each line of the file contains a row of the adjacency matrix,
    with each entry separated by any number of spaces.
    """
    with open(path, "r") as f:
        graph = [
            [int(x) for x in line.split()]
            for line in f.readlines()
            if line.strip() != ""
        ]
    return graph


def get_nx_graph(graph: AdjacencyMatrix):
    G = nx.from_numpy_array(np.array(graph), parallel_edges=False)
    return G


def arrange_graph(graph: nx.Graph):
    pos = nx.spring_layout(graph)
    return pos


def plot_graph(graph: nx.Graph, pos: dict[int, tuple[int, int]] = None):
    nx.draw(graph, with_labels=True, pos=pos)

    pos = arrange_graph(graph) if pos is None else pos
    labels = nx.get_edge_attributes(graph, "weight")

    nx.draw_networkx_edge_labels(graph, pos, edge_labels=labels)

    return graph


def plot_side_by_side(graph1: AdjacencyMatrix, graph2: AdjacencyMatrix):
    plt.subplot(1, 2, 1)
    plt.title("Graph")
    G1 = get_nx_graph(graph1)
    # Layout the graph once and use the same positions for both graphs
    pos = arrange_graph(G1)
    plot_graph(G1, pos=pos)

    plt.subplot(1, 2, 2)
    plt.title("MST")
    G2 = get_nx_graph(graph2)
    plot_graph(G2, pos=pos)

    plt.show()


def find_mst_prim(graph: AdjacencyMatrix):
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
            print(f"Verificando nó {m}")
            if not node_selected[m]:
                print(f"\tNó {m} não selecionado")
            else:
                print(f"\tNó {m} já selecionado!")
                for n in range(N):
                    print(f"\t\tVerificando aresta ({m}, {n})")
                    if not graph[m][n]:
                        print(f"\t\t\tNão há aresta")
                    elif node_selected[n]:
                        print(f"\t\t\tHá aresta, mas o nó {n} já foi selecionado")
                    else:
                        print(f"\t\t\tHá aresta e o nó {n} não foi selecionado!")
                        if minimum > graph[m][n]:
                            minimum = graph[m][n]
                            a = m
                            b = n
                            print(
                                f"\t\t\t\tAtualizando aresta: ({a}, {b}), custo: {minimum}"
                            )

        print("-" * 40)
        print(f"Adicionando aresta {no_edge}: ({a}, {b}), custo: {minimum}")
        print("-" * 40)
        mst[a][b] = minimum
        mst[b][a] = minimum

        node_selected[b] = True
        no_edge += 1

    return mst


def main():
    graph = load_graph_from_file(INPUT_PATH)
    mst = find_mst_prim(graph)
    plot_side_by_side(graph, mst)


if __name__ == "__main__":
    main()
