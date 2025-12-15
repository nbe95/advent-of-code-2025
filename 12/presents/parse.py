from .region import Region
from .shape import Shape


def parse_input(lines: list[str]) -> tuple[dict[int, Shape], list[Region]]:
    shape_lines: dict[int, list[str]] = {}
    region_lines: list[str] = []
    shape_index: int = -1

    for line in (line.strip() for line in lines):
        if not line:
            continue

        # New region definition
        if "x" in line and ":" in line:
            region_lines.append(line)

        # New shape definition
        elif line.endswith(":"):
            shape_index = int(line[:-1])
            shape_lines[shape_index] = []

        # Still ongoing shape definition
        else:
            shape_lines[shape_index].append(line)

    # Convert to actual objects
    shapes: dict[int, Shape] = {index: Shape(lines) for index, lines in shape_lines.items()}
    regions: list[Region] = [Region.from_string(line) for line in region_lines]
    return shapes, regions
