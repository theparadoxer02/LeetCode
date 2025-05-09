class Graph:
    def __init__(self):
        self.graph = {
            'A': {'B': 1, 'C': 5},
            'B': {'D': 2, 'E': 10}
        }

    def krushkal_algorithm(self, star_node, target_node):
        for node, dist in self.graph[star_node].items():
            for child_node, curr_child_dist in self.graph[node].items():
                new_distance = curr_child_dist + dist
                if new_distance < curr_child_dist:
                    self.graph[child_node] = new_distance

