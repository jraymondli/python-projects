Dijkstra's algorithm is used to find the shortest path between nodes in a graph. Here's an overview and a working Python example.

## Steps of Dijkstra's Algorithm
1. **Initialize Distances**: Set the distance to the source node to 0 and all other nodes to infinity.
2. **Visited Set**: Maintain a set of visited nodes to avoid reprocessing.
3. **Priority Queue**: Use a priority queue (or a min-heap) to always process the node with the smallest known distance.
4. **Relaxation**: For the current node, check its neighbors. If the total cost of the path to a neighbor is smaller than the known cost, update it.
5. **Repeat**: Continue until all nodes are processed or the shortest path to the target node is found.

## Python Implementation
Here’s a Python implementation using the `heapq` module for the priority queue:

```python
import heapq

def dijkstra(graph, start):
    """
    Finds the shortest paths from the start node to all other nodes in the graph.

    :param graph: A dictionary where keys are node names and values are lists of tuples (neighbor, weight)
    :param start: The starting node
    :return: A dictionary of the shortest paths to each node
    """
    # Priority queue to process the next most promising node
    priority_queue = []
    # Distances dictionary
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    # Push the start node with a distance of 0
    heapq.heappush(priority_queue, (0, start))

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Skip if the distance in the queue is not up-to-date
        if current_distance > distances[current_node]:
            continue

        # Relaxation step
        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            # If a shorter path to the neighbor is found
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Example graph (Adjacency list)
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('A', 1), ('C', 2), ('D', 6)],
    'C': [('A', 4), ('B', 2), ('D', 3)],
    'D': [('B', 6), ('C', 3)],
}

# Running the algorithm
start_node = 'A'
shortest_paths = dijkstra(graph, start_node)

# Output results
print(f"Shortest paths from {start_node}:")
for node, distance in shortest_paths.items():
    print(f"Node {node}: Distance {distance}")
```
### Notes

1. The check `current_distance > distances[current_node]` is needed as we may have enqueued multiple distrance update on a node based on multiple nodes that are closer to the source than this node.


### Example Graph
The graph in the example above is represented as an adjacency list:
- `A` is connected to `B` with weight 1 and to `C` with weight 4.
- `B` is connected to `A`, `C`, and `D` with weights 1, 2, and 6 respectively.
- `C` is connected to `A`, `B`, and `D` with weights 4, 2, and 3 respectively.

### Output for the Example
For the graph given, running the algorithm from `A` would give:
```
Shortest paths from A:
Node A: Distance 0
Node B: Distance 1
Node C: Distance 3
Node D: Distance 6
```

This implementation is efficient and works for graphs with non-negative weights. 

## References

- https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm


