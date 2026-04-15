class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_node(self, name):
        if name not in self.adj_list:
            self.adj_list[name] = []

    def add_edge(self, start, end, cost):
        self.add_node(start)
        self.add_node(end)
        self.adj_list[start].append((end, float(cost)))

    def get_neighbors(self, node):
        return self.adj_list.get(node, [])

    def bfs(self, start):
        if start not in self.adj_list:
            return []

        visited = {start}
        queue = [start]
        order = []
        front_index = 0

        while front_index < len(queue):
            current = queue[front_index]
            front_index += 1
            order.append(current)

            for neighbor, _ in self.get_neighbors(current):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start):
        if start not in self.adj_list:
            return []

        visited = set()
        order = []

        def explore(node):
            visited.add(node)
            order.append(node)
            for neighbor, _ in self.get_neighbors(node):
                if neighbor not in visited:
                    explore(neighbor)

        explore(start)
        return order

    def dijkstra(self, start, end, min_heap):
        if start not in self.adj_list or end not in self.adj_list:
            return None, float('inf')

        distance = {node: float('inf') for node in self.adj_list}
        parent = {node: None for node in self.adj_list}
        distance[start] = 0.0
        min_heap.insert((0.0, start))

        while not min_heap.is_empty():
            current_distance, current_node = min_heap.extract_min()

            if current_distance > distance[current_node]:
                continue

            if current_node == end:
                break

            for neighbor, edge_cost in self.get_neighbors(current_node):
                new_distance = current_distance + edge_cost
                if new_distance < distance[neighbor]:
                    distance[neighbor] = new_distance
                    parent[neighbor] = current_node
                    min_heap.insert((new_distance, neighbor))

        if distance[end] == float('inf'):
            return None, float('inf')

        path = []
        current = end
        while current is not None:
            path.append(current)
            current = parent[current]
        path.reverse()
        return path, distance[end]

    def detect_cycles(self):
        white = 0
        gray = 1
        black = 2
        color = {node: white for node in self.adj_list}
        parent = {node: None for node in self.adj_list}

        def visit(node):
            color[node] = gray

            for neighbor, _ in self.get_neighbors(node):
                if color[neighbor] == white:
                    parent[neighbor] = node
                    cycle = visit(neighbor)
                    if cycle:
                        return cycle
                elif color[neighbor] == gray:
                    cycle_nodes = [neighbor]
                    current = node
                    while current is not None and current != neighbor:
                        cycle_nodes.append(current)
                        current = parent[current]
                    cycle_nodes.append(neighbor)
                    cycle_nodes.reverse()
                    return cycle_nodes

            color[node] = black
            return None

        for node in self.adj_list:
            if color[node] == white:
                cycle = visit(node)
                if cycle:
                    return True, cycle
        return False, []

    def connected_components_count(self):
        visited = set()
        components = 0

        undirected = {node: [] for node in self.adj_list}
        for node, neighbors in self.adj_list.items():
            for neighbor, _ in neighbors:
                undirected[node].append(neighbor)
                undirected[neighbor].append(node)

        for node in self.adj_list:
            if node in visited:
                continue
            components += 1
            stack = [node]
            visited.add(node)

            while stack:
                current = stack.pop()
                for neighbor in undirected[current]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

        return components
