from dataclasses import dataclass

from .shape import Shape


@dataclass
class Region:

    width: int
    height: int
    shape_count: list[int]

    @classmethod
    def from_string(cls, line: str) -> "Region":
        size, occurrences = line.split(":")
        width, height = map(int, size.split("x"))
        shape_count: list[int] = list(map(int, occurrences.strip().split()))
        return cls(width, height, shape_count)

    @property
    def total_area(self) -> int:
        return self.width * self.height

    def could_fit(self, shape_def: dict[int, Shape]) -> bool:

        # Trivial case 1:
        # Area occupied by all shapes together is bigger than total area of this region

        if self.total_area < sum(
            shape_def[index].area * count for index, count in enumerate(self.shape_count)
        ):
            return False

        # Trivial case 2:
        # Even when aligned "dumb" (each shape next to each other), the shapes' total area does not
        # exceed this region's area

        if self.total_area >= sum(
            shape_def[index].border_area * count for index, count in enumerate(self.shape_count)
        ):
            return True

        # Hard case: Maybe solve this in future... :)
        raise NotImplementedError("Actual packing problem left as an exercise for the reader.")
