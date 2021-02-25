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
    if n>1:
        if n > MinimalLinkRule+1:
            print("Adding a random number of link")
            NumberOfLink = random.randint(MinimalLinkRule, MaximalLinkRule)
            for i in range(0,NumberOfLink-2):
                StartNodeIndex = n-1
                EndNodeIndex = random.choice(nodeList)
                print(nodeList)
                nodeList.remove(EndNodeIndex)
                G.add_edge(*(str(StartNodeIndex), str(EndNodeIndex)))
        else:
            print("Adding link between firsts node")
            for i in range(0, n-1):
                StartNodeIndex = n-1
                EndNodeIndex = i
                G.add_edge(*(str(StartNodeIndex), str(EndNodeIndex)))

def SimulateLinkBetweeTwoNode(G):
    print("hello")

def main():
    G = nx.Graph()
    for i in range(0,10):
        print("Iterations"+str(i))
        AddNodePlusRandomLink(G)

    nx.draw(G, with_labels=True, font_weight="bold")
    plt.show()
    print("Done")

if __name__== "__main__":
    main()