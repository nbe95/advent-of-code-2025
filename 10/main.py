"""Advent of Code - 2025-12-10"""

import sys

from machine import Machine


def main() -> int:

    with open(sys.path[0] + "/input.txt", "r") as handle:

        total_lights: int = 0
        total_joltage: int = 0
        for index, line in enumerate(handle.readlines()):
            machine = Machine(line)
            presses_lights: int = machine.calc_fewest_presses_for_lights()
            presses_joltage: int = machine.calc_fewest_presses_for_joltage()
            total_lights += presses_lights
            total_joltage += presses_joltage
            print(
                f"Machine {index+1}: {presses_lights} presses for lights, "
                f"{presses_joltage} for joltage levels."
            )

        print(f"Total sum of button presses for correct lights to shine: {total_lights}")
        print(f"Total sum of button presses for correct joltage levels: {total_joltage}")

    return 0


if __name__ == "__main__":
    main()
