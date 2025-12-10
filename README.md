# Advent of Code 2025

Python solutions for [Advent of Code 2025](https://adventofcode.com/2025/).
Daily tasks are organized in respective subdirectories with `main.py` script as entry point.
Each day's individual puzzle input needs to be placed as `ìnput.txt` file inside each subdirectory.

## pdm scripts

- `pdm day nn`: Run script for day _n_.
- `pdm test`: Run all unit tests.
- `pdm format`: Format entire code.
- `pdm lint nn`: Run linter and code checkers for day _n_.
- `pdm input nn`: Fetch and store puzzle input for day _n_.
  - _SESSION_ID_ must be specified in `.env` file.

## Evaluation and Findings

- Day 01
  - Test first, code later.
- Day 02
  - The first solution that comes to mind is presumably not the best/fastest/easiest one.
  - Requirements changed? Starting anew can be better and faster than modifying the existing solution.
- Day 03
  - The best software design is only as good as it fits real-world input.
- Day 05
  - Optimization _does_ matter.
- Day 09
  - A good drawing beats hours of thinking.
- Day 10
  - Not ignoring hints like _"-0.5 button presses"_ makes it way easier to rethink what the actual
    (type of) problem is.
