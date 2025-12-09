import re
from functools import reduce
from operator import mul


class OpMatrix:

    def __init__(self, lines: list[str]):
        self._cols: list[list[int | str]] = []
        for row in lines:
            items: list[str] = row.split()
            if not self._cols:
                self._cols = [[] for _ in range(len(items))]
            for index, item in enumerate(items):
                self._cols[index].append(item)

    def calc_cols(self) -> list[int]:
        total: list[int] = []
        for col in self._cols:
            values: map = map(int, col[:-1])
            operator: str = str(col[-1])
            if operator == "+":
                total.append(sum(values))
            elif operator == "*":
                total.append(reduce(mul, values, 1))
            else:
                raise ValueError(f"Unknown operator: {operator}")
        return total

    def get_grand_total(self) -> int:
        return sum(self.calc_cols())


class OpMatrixRtl(OpMatrix):

    # pylint: disable=super-init-not-called
    def __init__(self, lines: list[str]):
        # Goal: Transform input data at initial parsing to match structure of OpMatrix
        self._cols: list[list[int | str]] = []

        col_offset: int = 0
        col_width: int = 0
        while True:
            # First, find operator and width of each column by looking at the last line
            operator: str = lines[-1][col_offset]

            next_op = re.search(r"[+*]", lines[-1][col_offset + 1 :])
            if next_op:
                col_width = next_op.start()
            else:
                col_width = max(len(line) - col_offset for line in lines)

            # Parse individual digits of numbers (x/y represent relative character positions)
            values: list[int] = []
            for x in range(col_offset + col_width - 1, col_offset - 1, -1):
                number: int = 0
                for y in range(0, len(lines) - 1):
                    if x >= len(lines[y]):
                        continue
                    digit: str = lines[y][x]
                    if digit == " ":
                        continue
                    number = number * 10 + int(digit)
                values.append(number)

            self._cols.append([*values, operator])

            # Find beginning of next column or abort if no more columns left
            col_offset += col_width + 1
            if col_offset > len(lines[-1]):
                break
