def find_pattern_twice(id_range: str) -> set[int]:
    start, end = map(int, id_range.split("-"))

    def is_repetitive(value: str) -> bool:
        first_half, last_half = value[: len(value) // 2], value[len(value) // 2 :]
        return first_half == last_half

    return {value for value in range(start, end + 1) if is_repetitive(str(value))}


def find_pattern_multiple(id_range: str) -> set[int]:
    start, end = map(int, id_range.split("-"))
    result: set[int] = set()

    def is_repetitive(value: str, chunk_len: int) -> bool:
        # Only check if dividable by chunk_len and shorter than half length
        if len(value) % chunk_len != 0 or len(value) < chunk_len * 2:
            return False

        n: int = len(value) // chunk_len
        return value == value[:chunk_len] * n

    for length in range(1, len(str(end))):
        result.update(
            {value for value in range(start, end + 1) if is_repetitive(str(value), length)}
        )
    return result
