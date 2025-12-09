class TachyonManifold:

    def __init__(self, grid: list[str]):
        self._grid: list[str] = grid

    def _get_cell(self, row: int, col: int) -> str:
        if row not in range(len(self._grid)):
            return ""
        if col not in range(len(self._grid[row])):
            return ""
        return self._grid[row][col]

    def _set_cell(self, row: int, col: int, char: str) -> None:
        if row not in range(len(self._grid)):
            return
        if col not in range(len(self._grid[row])):
            return
        self._grid[row] = self._grid[row][:col] + char[:1] + self._grid[row][col + 1 :]

    def process_beam(self) -> None:
        for y in range(1, len(self._grid)):
            for x in range(len(self._grid[0])):

                # Process each character in the x/y matrix
                above: str = self._get_cell(y - 1, x)
                current: str = self._get_cell(y, x)

                if current == ".":
                    if above in ("S", "|"):
                        self._set_cell(y, x, "|")

                elif current == "^" and above == "|":
                    self._set_cell(y, x - 1, "|")
                    self._set_cell(y, x + 1, "|")

    def count_splits(self) -> int:
        result: int = 0
        for y in range(1, len(self._grid)):
            for x in range(len(self._grid[0])):
                above: str = self._get_cell(y - 1, x)
                current: str = self._get_cell(y, x)
                if current == "^" and above in ("S", "|"):
                    result += 1
        return result

    def count_paths(self) -> int:
        # Traverse binary tree bottom-up

        # Matrix with same dimensions as self._grid with each value = possible paths to leafs
        height: int = len(self._grid)
        width: int = max(len(row) for row in self._grid)
        paths: list[list[int]] = [[0 for _ in range(width)] for _ in range(height + 1)]

        # Add extra row for leaf nodes with 1 resulting end path each
        for x in range(width):
            paths[height][x] = 1 if self._get_cell(height - 1, x) == "|" else 0

        # Iterate from bottom to top
        for y in range(height - 1, -1, -1):
            for x in range(width):
                current: str = self._get_cell(y, x)

                if current in ("S", "|"):
                    # apply path from cell below
                    paths[y][x] = paths[y + 1][x]

                elif current == "^":
                    # add up possible paths to the left and right
                    paths_left: int = paths[y + 1][x - 1] if x > 0 else 0
                    paths_right: int = paths[y + 1][x + 1] if x < width - 1 else 0
                    paths[y][x] = paths_left + paths_right

        # Find resulting number of paths at root node
        root_x: int = self._grid[0].index("S")
        root_y: int = 0
        return paths[root_y][root_x]
