# Template for building a graph
class graph:
    def __init__(self):
        self.graph_list = {}

    def build_graph(self, dependencies):
        for dependency in dependencies:
            parent, child = dependency[1], dependency[0]
            if parent not in self.graph_list:
                self.graph_list[parent] = []
            self.graph_list[parent].append(child)
