"""Advent of Code - 2025-12-11"""

import sys

from graph import DirectedAcyclicGraph


def main() -> int:

    with open(sys.path[0] + "/input.txt", "r") as handle:

        graph = DirectedAcyclicGraph(handle.readlines())
        print(f"Created Graph with {graph.nodes} nodes and {graph.edges} edges.")

        you_out: int = graph.count_simple_paths("you", "out")
        print(f"Number of paths 'you' -> 'out': {you_out}")

        svr_fft: int = graph.count_simple_paths("svr", "fft")
        print(f"Number of paths 'svr' -> 'fft': {svr_fft}")

        fft_dac: int = graph.count_simple_paths("fft", "dac")
        print(f"Number of paths 'fft' -> 'dac': {fft_dac}")

        dac_out: int = graph.count_simple_paths("dac", "out")
        print(f"Number of paths 'day' -> 'out': {dac_out}")

        num_paths: int = svr_fft * fft_dac * dac_out
        print(f"Number of paths 'svr' -> 'fft' -> 'dac' -> 'out': {num_paths}")

    return 0


if __name__ == "__main__":
    main()
