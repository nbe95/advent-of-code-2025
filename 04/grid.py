class PaperGrid:
    def __init__(self, grid: list[str]):
        self._grid: list[str] = grid

    def get_cell(self, row: int, col: int) -> str:
        if row not in range(len(self._grid)):
            return ""
        if col not in range(len(self._grid[row])):
            return ""
        return self._grid[row][col]

    def get_adjacent_cells(self, row: int, col: int) -> str:
        result: str = ""
        for y in range(row - 1, row + 2):
            for x in range(col - 1, col + 2):
                if y != row or x != col:
                    result += self.get_cell(y, x)
        return result

    def remove_accessible_rolls(self) -> int:
        new_grid: list[str] = []
        count: int = 0
        for row in range(len(self._grid)):
            new_grid_row = ""
            for col in range(len(self._grid[row])):
                if (
                    self.get_cell(row, col) == "@"
                    and self.get_adjacent_cells(row, col).count("@") < 4
                ):
                    count += 1
                    new_grid_row += "x"
                else:
                    new_grid_row += self.get_cell(row, col)
            new_grid.append(new_grid_row)
        self._grid = new_grid
        return count
