from graph import DirectedAcyclicGraph

graph1 = DirectedAcyclicGraph(
    [
        "aaa: you hhh",
        "you: bbb ccc",
        "bbb: ddd eee",
        "ccc: ddd eee fff",
        "ddd: ggg",
        "eee: out",
        "fff: out",
        "ggg: out",
        "hhh: ccc fff iii",
        "iii: out",
    ]
)
graph2 = DirectedAcyclicGraph(
    [
        "svr: aaa bbb",
        "aaa: fft",
        "fft: ccc",
        "bbb: tty",
        "tty: ccc",
        "ccc: ddd eee",
        "ddd: hub",
        "hub: fff",
        "eee: dac",
        "dac: fff",
        "fff: ggg hhh",
        "ggg: out",
        "hhh: out",
    ]
)


def test_graph() -> None:
    assert graph1.nodes == 11
    assert graph1.edges == 17

    assert graph2.nodes == 14
    assert graph2.edges == 16


def test_find_paths() -> None:
    paths1 = graph1.find_simple_paths("you", "out")

    assert len(paths1) == 5
    assert ("you", "bbb", "ddd", "ggg", "out") in paths1
    assert ("you", "bbb", "eee", "out") in paths1
    assert ("you", "ccc", "ddd", "ggg", "out") in paths1
    assert ("you", "ccc", "eee", "out") in paths1
    assert ("you", "ccc", "fff", "out") in paths1

    paths2 = graph2.find_simple_paths("svr", "out")

    assert len(paths2) == 8
    assert ("svr", "aaa", "fft", "ccc", "ddd", "hub", "fff", "ggg", "out") in paths2
    assert ("svr", "aaa", "fft", "ccc", "ddd", "hub", "fff", "hhh", "out") in paths2
    assert ("svr", "aaa", "fft", "ccc", "eee", "dac", "fff", "ggg", "out") in paths2
    assert ("svr", "aaa", "fft", "ccc", "eee", "dac", "fff", "hhh", "out") in paths2
    assert ("svr", "bbb", "tty", "ccc", "ddd", "hub", "fff", "ggg", "out") in paths2
    assert ("svr", "bbb", "tty", "ccc", "ddd", "hub", "fff", "hhh", "out") in paths2
    assert ("svr", "bbb", "tty", "ccc", "eee", "dac", "fff", "ggg", "out") in paths2
    assert ("svr", "bbb", "tty", "ccc", "eee", "dac", "fff", "hhh", "out") in paths2


def test_count_paths() -> None:
    assert graph1.count_simple_paths("you", "out") == 5

    assert graph2.count_simple_paths("svr", "fft") == 1
    assert graph2.count_simple_paths("fft", "dac") == 1
    assert graph2.count_simple_paths("dac", "out") == 2
