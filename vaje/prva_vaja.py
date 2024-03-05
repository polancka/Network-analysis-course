import networkx as nx
import matplotlib.pyplot as py

#creating a graph
G = nx.Graph()
# nx.DiGraph / nx.MultiGraph / nx.MultiDiGraph

#adding nodes and edges
G.add_node(1)
G.add_node(2)
G.add_edge(1,2)

#visualizing the graph 

#Inspecting a graph
print(list(G.neighbors(1))) #lists all neighbours of node 1
print(list(G[1])) # will do the same

#transversing all nodes and for every node their neighbours
for i in G.nodes:
    for j in G[i]: 
        print("neki")

#when printing edges, the nodes of an edge will be printed in an alphabetcial order if not stated otherwise
#degree: 
print(G.degree) #the size of the network
len(G) #number of nodes == range(len(G)) to loop trough 

#converting a graph to diGraph
D = nx.DiGraph(G) 

#when the graph is transformed -> every undirected edge is tranformed into two directed edges
#now the order in the tuples od the edge nodes matters because we have dirrected edges

#predecesors - they point to node i
#sucessors - node i points to them

# transforming to multigraph: we tale the undirected graph G and trasform it
M = nx.MultiGraph(G)
M.add_edge("foo", "bar", label = "new")

#we can also transform it to a weighted graph! we can weight the edges
#having two weighted edges from node i to node j is not the same as having one edge that has the weight that sums the other two edges 
#depends on the case

#Neighbours are returned withouth večkratnost (same node is only printed once even if there are more edges betwen those two nodes)
#Dictionary : keys are numbers of edges, values are new dictionaries that have some new information about the edge
# we need to check how big this dictionary is to actually take into the account the double edges (looping trough neighbours will leave out the double edges)

G.edges(i) # will give a list of tuples

#multidigraph work similarly (look it up at home)
#when adding edges be careful (error or making up new edges)

#random graph models- algorithms for consturcting graphs
#G(n,m) model -> it creates a random graph with n nodes and m edges

#How many edges would we need if we have 100 nodes to say with a great ecrtanty that the graph will be connected (no isolated islands)

#Dolphins network - which dolphins swam togheter

#pajek format (chech the name)
# *vertices 62
# 1 "Beak" 2
# 2 "Beescratch" 1
# .... all the nodes
# *edges 102 (these are undirected)
# 11 1
# 12 2
# ... all the edges

# if we wanted directed edges we would say
# *arcs 103
# ... directed edges listed

#we must convert node labels to integers if we are reading from such file/format
G = nx.convert_node_labels_to_integers(G, label_attribute= "label")

#Importance of nodes: measure of CENTRALITY: page rank algorithm, 
scores = nx.pagerank(G)
sizes = [1e4 * scores[i] for i in G.nodes()]
#draw(G, node_size = sizes) #import the draw function from the noteebok

#partitioning the network - community detection (we want the algorithm to figure out how many groups there are)
#label propagation algorithm that returns a list of sets, each set represents one of the detected groups
#if there is no grouping  it will return one set of all the nodes 
