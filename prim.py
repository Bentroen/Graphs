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


def main():
    graph = load_graph_from_file(INPUT_PATH)
    print(graph)

    plot_graph(graph)


if __name__ == "__main__":
    main()
