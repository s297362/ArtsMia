import networkx as nx

import database.DAO


class Model:
    def __init__(self):
        self.graph = nx.Graph()
        self.idMap = {}

    def buildGraph(self):
        oggetti = database.DAO.DAO().getOggetti()
        for o in oggetti:
            self.graph.add_node(o.object_id)
            self.idMap[o.object_id] = o
        archi = database.DAO.DAO().getArchi()
        for a in archi:
            self.graph.add_edge(a.o1, a.o2, weight=a.weight)
        return self.graph

    def componenteConnessa(self, objId):
        compConn = nx.node_connected_component(self.graph, objId)
        return compConn