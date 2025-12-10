import re

import numpy as np
from scipy.optimize import Bounds, LinearConstraint, milp


class Machine:

    def __init__(self, line: str):
        match = re.fullmatch(r"\[([.#]+)\] ((?:\([\d,]+\) )+)\{([\d,]+)\}", line.strip())
        if not match:
            raise ValueError(f"Invalid machine definition: {line}")

        # Lights as bit combination
        self._lights: int = sum(1 << i for i, char in enumerate(match.group(1)) if char == "#")
        self._buttons: list[tuple[int, ...]] = [
            tuple(map(int, tuples[1:-1].split(",")))
            for tuples in match.group(2).split(" ")
            if tuples
        ]
        self._joltage: list[int] = list(map(int, match.group(3).split(",")))

        # Create bit masks from button integer values for faster operation
        self._button_masks: list[int] = [sum(1 << i for i in index) for index in self._buttons]

    def press_light_btn(self, button: int, status: int) -> int:
        # Button press = XOR
        return status ^ self._button_masks[button]

    def calc_fewest_presses_for_lights(self) -> int:
        """Find the fewest number of button presses required to light up the desired lights (BFS)"""
        num_presses: int = 0
        permutations: list[int] = [0]
        while True:
            num_presses += 1
            new_perm: list[int] = []
            for perm in permutations:
                new_perm.extend(
                    self.press_light_btn(btn, perm) for btn, _ in enumerate(self._buttons)
                )

            if self._lights in new_perm:
                return num_presses
            permutations = new_perm

    def calc_fewest_presses_for_joltage(self) -> int:
        """Find the fewest number of button presses required to get the desired joltage levels. This
        is a linear algebra problem, which requires a matrix equation solver (ILP)."""

        # Convert the coefficients (=buttons) from [1, 3] to [0, 1, 0, 1]
        buttons: list[list[int]] = [
            [1 if i in button else 0 for i, _ in enumerate(self._joltage)]
            for button in self._buttons
        ]
        coefficients = np.matrix_transpose(buttons)
        solution = np.array(self._joltage)

        num_buttons: int = len(self._buttons)
        result = milp(
            c=np.ones(num_buttons),  # cost vector (minimize total sum)
            constraints=LinearConstraint(coefficients, solution, solution),  # linear constraint
            integrality=np.ones(num_buttons),  # only whole numbers
            bounds=Bounds(lb=0, ub=np.inf),  # bounds
        )

        if not result.success:
            raise ValueError("MILP failed")

        return int(sum(map(np.round, result.x)))  # sum of button presses
