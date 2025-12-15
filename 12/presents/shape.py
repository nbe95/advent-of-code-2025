class Shape:

    def __init__(self, lines: list[str]):
        self.height: int = len(lines)
        self.width: int = max(len(line) for line in lines)

        # Store occupied tiles as bit matrix for easier overlapping detection
        self._occupied_bits: int = 0
        for line_no, line in enumerate(lines):
            self._occupied_bits += sum(
                1 << (i + line_no * self.width) for i, c in enumerate(line) if c == "#"
            )

    @property
    def area(self) -> int:
        return self._occupied_bits.bit_count()

    @property
    def border_area(self) -> int:
        return self.width * self.height

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Shape):
            return NotImplemented

        return (
            self.height == other.height
            and self.width == other.width
            and self._occupied_bits == other._occupied_bits
        )
