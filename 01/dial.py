class Dial:
    def __init__(self, start_pos: int = 50):
        self._pos: int = start_pos
        self._count: dict[int, int] = {}
        self._count_with_ticks: dict[int, int] = {}

    def rotate(self, command: str) -> None:
        steps: int = int(command[1:])
        match command[0].upper():
            case "L":
                steps *= -1
            case "R":
                pass
            case _:
                raise ValueError(f"Invalid command: {command}")

        ticks_in_between: list[int] = range(self._pos + steps, self._pos, 1 if steps < 0 else -1)
        for tick in ticks_in_between:
            tick %= 100
            self._count_with_ticks[tick] = self._count_with_ticks.get(tick, 0) + 1

        self._pos = (self._pos + steps) % 100
        self._count[self._pos] = self._count.get(self._pos, 0) + 1

    def get_pos(self) -> int:
        return self._pos

    def count(self, pos: int, with_ticks: bool = False) -> int:
        if with_ticks:
            return self._count_with_ticks.get(pos, 0)
        return self._count.get(pos, 0)
