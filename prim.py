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


def main():
    graph = load_graph_from_file(INPUT_PATH)
    print(graph)


if __name__ == "__main__":
    main()
