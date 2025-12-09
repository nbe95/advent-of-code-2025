from dataclasses import dataclass


@dataclass
class Tile:
    x: int
    y: int

    @classmethod
    def from_string(cls, line: str) -> "Tile":
        return cls(*map(int, line.split(",")))

    def calc_area_to(self, other: "Tile") -> int:
        return (abs(self.x - other.x) + 1) * (abs(self.y - other.y) + 1)

    def calc_direct_path_to(self, other: "Tile") -> list["Tile"]:
        if self.x == other.x:
            start = self.y + (1 if self.y < other.y else -1)
            end = other.y + (-1 if self.y < other.y else 1)
            step = 1 if self.y < other.y else -1

            return [Tile(self.x, y) for y in range(start, end + step, step)]

        elif self.y == other.y:
            start = self.x + (1 if self.x < other.x else -1)
            end = other.x + (-1 if self.x < other.x else 1)
            step = 1 if self.x < other.x else -1
            return [Tile(x, self.y) for x in range(start, end + step, step)]
        else:
            raise ValueError(
                f"Cannot find direct path between tiles not aligned on one common axis: {self}, {other}"
            )
