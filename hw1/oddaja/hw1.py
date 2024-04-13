# algorithm for finding strongly connected components in directed networks
import networkx as nx

#read nodes and edges from the file
def get_nodes_and_edges(file_path):
    G = nx.DiGraph(name = 'enron')

    with open(file_path, 'r') as file:
        # Read the first 87273 lines to extract nodes
        for _ in range(87273):
            line = next(file).strip()
            if line.startswith('*arcs'):
                break
            node_id = line.split()
            print(node_id)
            break
            G.add_node(int(node_id[0]) - 1, label = node_id[1])

        # Read arcs and edges
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith('*arcs'):
                continue
            source_node, target_node = map(int, line.split())
            G.add_edge(source_node, target_node)

    return G



def find_strong_componnent():
    return 0

file_path = "enron.net"
G = get_nodes_and_edges(file_path)

#number of  strongly connected components

#Size of the biggest one 