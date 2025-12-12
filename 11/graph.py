class DirectedAcyclicGraph:

    def __init__(self, lines: list[str]):

        self._nodes: set[str] = set()
        self._edges: dict[str, list[str]] = {}

        for line in lines:
            name, successors = line.split(":")
            self._nodes.add(name)

            successors_list: list[str] = [s for s in successors.split() if s]
            self._edges.update({name: successors_list})
            self._nodes.update(s for s in successors_list if s not in self._nodes)

    @property
    def nodes(self) -> int:
        return len(self._nodes)

    @property
    def edges(self) -> int:
        return sum(len(edges) for edges in self._edges.values())

    def find_simple_paths(
        self, start_node: str, end_node: str, visited: set[str] | None = None
    ) -> set[tuple[str, ...]]:
        """Trivial DFS algorithm with recursion retrieving all simple paths between two nodes."""
        if visited is None:
            visited = set()

        # Create copy (!) of visited and append current node
        current_visited = visited.union({start_node})

        # Target reached?
        if start_node == end_node:
            return {(start_node,)}

        all_paths: set = set()
        for next_node in self._edges.get(start_node, []):
            if next_node not in current_visited:
                paths_from_next = self.find_simple_paths(next_node, end_node, current_visited)
                for path in paths_from_next:
                    all_paths.add((start_node,) + path)
        return all_paths

    def count_simple_paths(self, start_node: str, end_node: str) -> int:
        """Optimized DFS algorithm counting all simple paths between two nodes."""
        # Since our graph is directed, sort nodes after topological appearance and save them as a
        # list. Thus, we need to traverse the graph once and can iterate over a lookup-table then to
        # find all simple paths.
        topological_stack: list[str] = self._topological_sort()
        path_counts: dict[str, int] = {node: 0 for node in self._nodes}
        path_counts[start_node] = 1

        for node in topological_stack:
            if path_counts[node] > 0:
                for successor in self._edges.get(node, []):
                    path_counts[successor] += path_counts[node]

        return path_counts[end_node]

    def _topological_sort(self) -> list[str]:
        # Create a single list of in which order all nodes need to be processed using DFS.
        visited: set[str] = set()
        recursion_stack: set[str] = set()
        result: list[str] = []

        def dfs_sort(node):
            visited.add(node)
            recursion_stack.add(node)

            for neighbor in self._edges.get(node, []):
                if neighbor not in visited:
                    dfs_sort(neighbor)
                elif neighbor in recursion_stack:
                    raise ValueError(f"Detected cycle in Graph: {node} -> {neighbor}")

            recursion_stack.remove(node)
            result.append(node)  # Append node after each successor has already been processed

        for node in self._nodes:
            if node not in visited:
                dfs_sort(node)

        return result[::-1]  # Return list in reverse order
