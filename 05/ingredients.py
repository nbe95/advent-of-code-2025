class IngredientDb:

    def __init__(self, lines: list[str]):
        separator: int = lines.index("")
        fresh_ranges: list[tuple[int, int]] = [
            tuple(map(int, r.split("-"))) for r in lines[:separator]  # type: ignore
        ]

        self._fresh_ranges: list[tuple[int, int]] = self.merge_ranges(fresh_ranges)
        self._available: set[int] = set(map(int, lines[separator + 1 :]))

    @staticmethod
    def merge_ranges(ranges: list[tuple[int, int]]) -> list[tuple[int, int]]:
        """Remove overlapping ranges, eliminating any duplicate entries"""
        if len(ranges) == 0:
            return []

        ranges.sort(key=lambda r: r[0])
        merged: list[tuple[int, int]] = []
        merged.append(ranges[0])

        for current_start, current_end in ranges[1:]:
            last_merged_start, last_merged_end = merged[-1]
            if current_start <= last_merged_end:
                # Overlapping? Update current merge area
                merged[-1] = (last_merged_start, max(last_merged_end, current_end))
            else:
                # Insert as new, non-overlapping range
                merged.append((current_start, current_end))
        return merged

    def get_fresh_and_available(self) -> set[int]:
        result: set[int] = set()
        for ingredient in self._available:
            for id_range in self._fresh_ranges:
                if ingredient in range(id_range[0], id_range[1] + 1):
                    result.add(ingredient)
                    break
        return result

    def count_fresh(self) -> int:
        return sum(fresh[1] - fresh[0] + 1 for fresh in self._fresh_ranges)
