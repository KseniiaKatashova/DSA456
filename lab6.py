
import heapq

def dijkstra(graph, start, target):
    # 1. Create a dictionary that will store the distances between the start node and all other nodes in the graph. 
    
    distances = {node: float('inf') for node in graph}              # set the distance of all other nodes to infinity
    distances[start] = 0                                            # set distance of the start node to 0 
    
   # 2. Create a dictionary that will store the previous node in the shortest path to each node. Set the previous node of the start node to None.
    previous = {node: None for node in graph}  # Set the previous node of the start node to None.

    # 3. Create a priority queue called unvisited that will store the unvisited nodes in the graph.
    unvisited = [(0, start)]  # Insert the start node with a priority of 0.

    # 4. While unvisited is not empty, do the following:
    while unvisited:
        current_distance, current_node = heapq.heappop(unvisited)

        # If the node is the target node, stop the algorithm and return the shortest path and its distance.
        if current_node == target:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = previous[current_node]
            path.reverse()
            return path, current_distance


        # For each neighbor of the current node, calculate the tentative distance from the start node to the neighbor
        for neighbor, weight in graph[current_node].items():
            tentative_distance = current_distance + weight


            # If the tentative distance is less than the current distance, update `distances` and `previous`
            if tentative_distance < distances[neighbor]:
                distances[neighbor] = tentative_distance
                previous[neighbor] = current_node
                heapq.heappush(unvisited, (tentative_distance, neighbor))     #Add the neighbor to `unvisited` with a priority equal to the tentative distance.

    return None # if the target node is not reached


graph = {
    'A': {'B': 2, 'C': 1},
    'B': {'A': 2, 'C': 2, 'D': 1},
    'C': {'A': 1, 'B': 2, 'D': 4, 'E': 3},
    'D': {'B': 1, 'C': 4, 'E': 1, 'F': 2},
    'E': {'C': 3, 'D': 1, 'F': 1},
    'F': {'D': 2, 'E': 1, 'G': 3},
    'G': {'F': 3}
}

#TESTING

# Calculate the shortest path A -> F
path, distance = dijkstra(graph, 'A', 'F')
print(f"Shortest path from A to F: {path}, distance: {distance}")

# Calculate the shortest path  B -> G
path, distance = dijkstra(graph, 'B', 'G')
print(f"Shortest path from B to G: {path}, distance: {distance}")