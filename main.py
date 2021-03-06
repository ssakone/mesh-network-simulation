"""
TODO :
Model the growth of the network under different condition
(number of link betwenn node, link densification, node pattern,small worldness)

"""

import networkx as nx
import random
import matplotlib.pyplot as plt
from nxsim import BaseNetworkAgent

"""
Take the Graph an an argument and add a new Node Connected to a random ammount on Other Node
"""

# Just like subclassing a process in SimPy
class NodeBehaviour(BaseNetworkAgent):
    def __init__(self, environment=None, agent_id=0, state=()):  # Make sure to have these three keyword arguments
        super().__init__(environment=environment, agent_id=agent_id, state=state)
        self.packetGenerationProbability = 0.05
        self.maxNumberOfPacketPerSecondAllowed = 100

    def run(self):
        """Simuate basic routing algorithm and generate random traffic toward a "random" node"""
        while True:
            if self.state['id'] == 1:
                self.zombify()
                yield self.env.timeout(1)
            else:
                yield self.env.event()

    def generateTraffic(self):
        normal_neighbors = self.get_neighboring_agents(state_id=0)
        for neighbor in normal_neighbors:
            if random.random() < self.bite_prob:
                neighbor.state['id'] = 1  # zombie
                print(self.env.now, self.id, neighbor.id, sep='\t')
                break

class NetworkTopology:
    def __init__(self):  # Make sure to have these three keyword arguments
        self.G = nx.Graph()

    def addNodePlusRandomLink(self):
        minimalLinkRule = 2
        minimalLinkRule = minimalLinkRule + 2
        maximalLinkRule = 5
        n = len(self.G.nodes())
        nodeList = list(self.G.nodes())
        self.G.add_node(str(n))
        n = len(self.G.nodes())
        if n>1: # we need at least two node to create a link
            if n > minimalLinkRule+1: # we cant create more link than node so
                # in the beginning the max n of link = n of node
                # once there are enough node, add a random number contained between two border
                numberOfLink = random.randint(minimalLinkRule, maximalLinkRule)
                for i in range(0,numberOfLink-2): # add the choosen number of link
                    startNodeIndex = n-1
                    endNodeIndex = random.choice(nodeList) # connect to a random node accros the graph
                    nodeList.remove(endNodeIndex) # ensure we double link a node by removing it from the drafting pool
                    self.G.add_edge(*(str(startNodeIndex), str(endNodeIndex)))
            else:
                for i in range(0, n-1):
                    startNodeIndex = n-1
                    endNodeIndex = i
                    self.G.add_edge(*(str(startNodeIndex), str(endNodeIndex)))

    def simulateLinkBetweeTwoNode(self,depart, arrival):
        hello = 1
        print(hello)


def main():
    network = NetworkTopology()
    for i in range(0, 80):
        network.addNodePlusRandomLink()
    nx.draw(network.G, with_labels=True, font_weight="bold")
    plt.show()

    print("Done")


if __name__ == "__main__":
    main()
