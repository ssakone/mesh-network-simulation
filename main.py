"""

un reseau

une methode qui fais une simulation de connection entre 2 node donné

une methode qui fais N simulation en appelant la fonction d'avant avec des node prise au hazard a chaque fois et compute la distribution de probabilité pour la latence et le débit

une methode qui ajoute un lien au hazard entre deux node entre deux rayon donné (plus long que X et plus petit que Y

un main ou faire des test
"""

import networkx as nx
import random
import matplotlib.pyplot as plt

MinimalLinkRule = 1
MaximalLinkRule = 8

"""
Take the Graph an an argument and add a new Node Connected to a random ammount on Other Node
"""
def AddNodePlusRandomLink(G):
    n = len(G.nodes())
    G.add_node(n)
    n = len(G.nodes())
    nodeList = list(G.nodes())
    if n>1:
        if n < MinimalLinkRule+1:
            NumberOfLink = random.randint(MinimalLinkRule, MaximalLinkRule + 1)
            for i in range(0,NumberOfLink):
                StartNodeIndex = n-1
                EndNodeIndex = random.choice(nodeList)
                nodeList.remove(EndNodeIndex)
                G.add_edge(*(str(StartNodeIndex), str(EndNodeIndex)))
        else:
            for i in range(0, n-1):
                StartNodeIndex = n
                EndNodeIndex = i
                G.add_edge(*(str(StartNodeIndex), str(EndNodeIndex)))

def SimulateLinkBetweeTwoNode(G):
    print("hello")

def main():
    G = nx.Graph()
    for i in range(0,10):
        AddNodePlusRandomLink(G)

    nx.draw(G)
    plt.show()
    print("Done")

if __name__== "__main__":
    main()