from .rect import TileRect
from .tile import Tile


class TileFloor:

    def __init__(self, lines: list[str]):
        self._red_tiles: list[Tile] = [Tile.from_string(line) for line in lines]

    @property
    def height(self) -> int:
        return max(tile.y for tile in self._red_tiles) + 3

    @property
    def width(self) -> int:
        return max(tile.x for tile in self._red_tiles) + 3

    def __str__(self) -> str:
        """String representation as in examples, only for debugging!"""
        result: str = ""
        for y in range(self.height):
            for x in range(self.width):
                if Tile(x, y) in self._red_tiles:
                    result += "#"
                else:
                    result += "."
            result += "\n"
        return result

    def get_largest_area(self, only_red_green: bool = False) -> int:
        rectangles_to_check: list[TileRect] = []

        # Find all possible rectangles matching our criteria
        for index1, tile1 in enumerate(self._red_tiles):
            for tile2 in self._red_tiles[index1 + 1 :]:

                rect = TileRect(tile1, tile2)
                valid: bool = True

                # Area consists of red and green areas only = only possible for one continuos
                # polygon if the path of red tiles does not intersect this area
                if only_red_green:

                    # Check each 2 adjacent red tiles
                    for index, poly1 in enumerate(self._red_tiles):
                        poly2 = self._red_tiles[(index + 1) % len(self._red_tiles)]
                        if rect.is_intersected_by(poly1, poly2):
                            valid = False
                            break

                if valid:
                    rectangles_to_check.append(rect)

        # Calculate actual size
        return max(rect.area for rect in rectangles_to_check)
