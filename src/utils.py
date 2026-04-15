import os


def load_data(filepath, graph, trie, hashmap, maxheap):
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")

    with open(filepath, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    section = None
    for raw_line in lines:
        line = raw_line.strip()
        if not line:
            continue

        if line in ["NODES", "EDGES", "PACKAGES"]:
            section = line
            continue

        parts = line.split()

        if section == "NODES":
            for node_name in parts:
                graph.add_node(node_name)
                trie.insert(node_name)
                hashmap.put(
                    node_name,
                    {
                        "location": node_name,
                        "capacity": 0,
                        "active_status": True,
                    },
                )

        elif section == "EDGES" and len(parts) == 3:
            start, end, cost = parts
            graph.add_edge(start, end, float(cost))

        elif section == "PACKAGES" and len(parts) == 4:
            package_id, priority, destination, weight = parts
            maxheap.insert((int(priority), package_id, destination, float(weight)))


def format_path(path):
    if not path:
        return "No path found"
    return " -> ".join(path)


def print_menu():
    print("\n===== Smart Network Logistics Engine =====")
    print("1. Display Network Summary")
    print("2. Find Shortest Path")
    print("3. Detect Cycles")
    print("4. Dispatch Highest-Priority Package")
    print("5. Search Depot by Name")
    print("6. Autocomplete Depot Name")
    print("7. Exit")
    print("==========================================")
