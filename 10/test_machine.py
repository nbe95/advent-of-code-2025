from machine import Machine


def test_light_buttons() -> None:

    machine = Machine("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}")

    assert machine.press_light_btn(0, 0b0000) == 0b1000
    assert machine.press_light_btn(1, 0b0000) == 0b1010
    assert machine.press_light_btn(2, 0b0000) == 0b0100
    assert machine.press_light_btn(3, 0b0000) == 0b1100
    assert machine.press_light_btn(4, 0b0000) == 0b0101
    assert machine.press_light_btn(5, 0b0000) == 0b0011

    assert machine.press_light_btn(0, 0b1111) == 0b0111
    assert machine.press_light_btn(1, 0b1111) == 0b0101
    assert machine.press_light_btn(2, 0b1111) == 0b1011
    assert machine.press_light_btn(3, 0b1111) == 0b0011
    assert machine.press_light_btn(4, 0b1111) == 0b1010
    assert machine.press_light_btn(5, 0b1111) == 0b1100


def test_presses_for_light() -> None:

    machine1 = Machine("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}")
    assert machine1.calc_fewest_presses_for_lights() == 2

    machine2 = Machine("[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}")
    assert machine2.calc_fewest_presses_for_lights() == 3

    machine3 = Machine("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}")
    assert machine3.calc_fewest_presses_for_lights() == 2


def test_presses_for_joltage() -> None:

    machine1 = Machine("[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}")
    assert machine1.calc_fewest_presses_for_joltage() == 10

    machine2 = Machine("[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}")
    assert machine2.calc_fewest_presses_for_joltage() == 12

    machine3 = Machine("[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}")
    assert machine3.calc_fewest_presses_for_joltage() == 11
