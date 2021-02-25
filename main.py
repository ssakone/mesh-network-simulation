"""
TODO :
Model the growth of the network under different condition
(number of link betwenn node, link densification, node pattern,small worldness)

"""

import networkx as nx
import random
import matplotlib.pyplot as plt
MinimalLinkRule = 2
MinimalLinkRule = MinimalLinkRule+2
MaximalLinkRule = 5

"""
Take the Graph an an argument and add a new Node Connected to a random ammount on Other Node
"""
def AddNodePlusRandomLink(G):
    n = len(G.nodes())
    nodeList = list(G.nodes())
    G.add_node(str(n))
    n = len(G.nodes())
    if n>1: # we need at least two node to create a link
        if n > MinimalLinkRule+1: # we cant create more link than node so in the beginning the max n of link = n of node
            # once there are enough node, add a random number contained between two border
            NumberOfLink = random.randint(MinimalLinkRule, MaximalLinkRule)
            for i in range(0,NumberOfLink-2): # add the choosen number of link
                StartNodeIndex = n-1
                EndNodeIndex = random.choice(nodeList) # connect to a random node accros the graph
                nodeList.remove(EndNodeIndex) # ensure we double link a node by removing it from the drafting pool
                G.add_edge(*(str(StartNodeIndex), str(EndNodeIndex)))
        else:
            for i in range(0, n-1):
                StartNodeIndex = n-1
                EndNodeIndex = i
                G.add_edge(*(str(StartNodeIndex), str(EndNodeIndex)))

def SimulateLinkBetweeTwoNode(G):
    hello = 1

def main():
    """
    G = nx.Graph()
    for i in range(0,10):
        AddNodePlusRandomLink(G)
    """
    G = nx.hkn_harary_graph(17, 42)
    nx.draw(G, with_labels=True, font_weight="bold")
    plt.show()

    print("Done")

if __name__== "__main__":
    main()