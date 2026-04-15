import os

from graph import Graph
from heap import MinHeap, MaxHeap
from hashmap import CustomHashMap
from trie import PrefixTrie
from utils import format_path, load_data, print_menu


def main():
    route_graph = Graph()
    dispatch_queue = MaxHeap()
    depot_table = CustomHashMap()
    name_index = PrefixTrie()

    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    data_file = os.path.join(base_dir, "data", "network.txt")

    try:
        load_data(data_file, route_graph, name_index, depot_table, dispatch_queue)
    except FileNotFoundError as error:
        print(error)
        return

    while True:
        print_menu()
        choice = input("Select an option: ").strip()

        if choice == "1":
            node_count = len(route_graph.adj_list)
            edge_count = sum(len(neighbors) for neighbors in route_graph.adj_list.values())
            component_count = route_graph.connected_components_count()
            print(f"Nodes: {node_count}")
            print(f"Edges: {edge_count}")
            print(f"Connected components: {component_count}")

        elif choice == "2":
            start = input("Enter source node: ").strip()
            end = input("Enter destination node: ").strip()
            path, total_cost = route_graph.dijkstra(start, end, MinHeap())

            if path is None:
                print(f"No path found from {start} to {end}.")
            else:
                print(f"Shortest path: {format_path(path)}")
                print(f"Total cost: {total_cost}")

        elif choice == "3":
            has_cycle, cycle_nodes = route_graph.detect_cycles()
            if has_cycle:
                print("Cycle detected in the network.")
                print(f"Cycle nodes: {format_path(cycle_nodes)}")
            else:
                print("No cycles detected.")

        elif choice == "4":
            package = dispatch_queue.extract_max()
            if package is None:
                print("No packages left to dispatch.")
            else:
                priority, package_id, destination, weight = package
                print(f"Dispatched package: {package_id}")
                print(f"Priority: {priority}")
                print(f"Destination: {destination}")
                print(f"Weight (kg): {weight}")

        elif choice == "5":
            depot_name = input("Enter depot name to search: ").strip()
            depot_info = depot_table.get(depot_name)
            if depot_info is None:
                print("Depot not found.")
            else:
                print(f"Depot: {depot_name}")
                print(f"Location: {depot_info['location']}")
                print(f"Capacity: {depot_info['capacity']}")
                print(f"Active: {depot_info['active_status']}")

        elif choice == "6":
            prefix = input("Enter prefix to search: ").strip()
            matches = name_index.autocomplete(prefix)
            if matches:
                print("Matches:")
                for name in matches:
                    print(f"- {name}")
            else:
                print("No matching depot names.")

        elif choice == "7":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
