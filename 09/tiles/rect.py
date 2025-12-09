from .tile import Tile


class TileRect:

    def __init__(self, tile1: Tile, tile2: Tile):
        self.x_min: int = min(tile1.x, tile2.x)
        self.x_max: int = max(tile1.x, tile2.x)
        self.y_min: int = min(tile1.y, tile2.y)
        self.y_max: int = max(tile1.y, tile2.y)

    @property
    def area(self) -> int:
        return (self.x_max - self.x_min + 1) * (self.y_max - self.y_min + 1)

    def is_intersected_by(self, tile1: Tile, tile2: Tile) -> bool:
        """Check if the (orthogonal) path between two tiles intersects the inside of this
        rectangle."""
        # No intersection possible with height or width = 1
        if self.x_min == self.x_max or self.y_min == self.y_max:
            return False

        line_x_min: int = min(tile1.x, tile2.x)
        line_x_max: int = max(tile1.x, tile2.x)
        line_y_min: int = min(tile1.y, tile2.y)
        line_y_max: int = max(tile1.y, tile2.y)

        if tile1.x == tile2.x:  # vertical line
            if self.x_min < tile1.x < self.x_max:
                return line_y_min < self.y_max and line_y_max > self.y_min
            return False

        if tile1.y == tile2.y:  # horizontal line
            if self.y_min < tile1.y < self.y_max:
                return line_x_min < self.x_max and line_x_max > self.x_min
            return False

        raise ValueError(
            f"Cannot find intersection between tiles not aligned on one common axis: "
            f"{tile1}, {tile2}"
        )
