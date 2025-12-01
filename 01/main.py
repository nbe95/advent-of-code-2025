"""Advent of Code - 2025-12-01"""

from dial import Dial


def task(lines: list[str]) -> None:
    dial = Dial()
    for command in lines:
        dial.rotate(command)

    print(f"Rotated the dial {len(lines)} times. Final position: {dial.get_pos()}.")
    print(f"Password: {dial.count(0)}.")
    print(f"Password with counting each tick: {dial.count(0, True)}.")


def main() -> int:
    with open("input.txt", "r") as handle:
        task(handle.readlines())


if __name__ == "__main__":
    main()
