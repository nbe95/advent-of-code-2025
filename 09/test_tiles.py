from tiles import Tile, TileFloor, TileRect


def test_max_area() -> None:
    floor = TileFloor(["7,1", "11,1", "11,7", "9,7", "9,5", "2,5", "2,3", "7,3"])
    assert floor.get_largest_area() == 50
    assert floor.get_largest_area(True) == 24


def test_intersection() -> None:
    assert TileRect(Tile(2, 2), Tile(5, 5)).is_intersected_by(Tile(3, 1), Tile(3, 6)) == True
    assert TileRect(Tile(2, 2), Tile(5, 5)).is_intersected_by(Tile(1, 3), Tile(6, 3)) == True
    assert TileRect(Tile(2, 2), Tile(5, 5)).is_intersected_by(Tile(3, 3), Tile(3, 4)) == True
    assert TileRect(Tile(2, 2), Tile(5, 5)).is_intersected_by(Tile(3, 3), Tile(4, 3)) == True
    assert TileRect(Tile(2, 2), Tile(5, 5)).is_intersected_by(Tile(3, 1), Tile(3, 3)) == True
    assert TileRect(Tile(2, 2), Tile(5, 5)).is_intersected_by(Tile(1, 3), Tile(3, 3)) == True
    assert TileRect(Tile(2, 2), Tile(5, 5)).is_intersected_by(Tile(3, 4), Tile(3, 6)) == True
    assert TileRect(Tile(2, 2), Tile(5, 5)).is_intersected_by(Tile(4, 3), Tile(6, 3)) == True
    assert TileRect(Tile(3, 3), Tile(3, 3)).is_intersected_by(Tile(3, 1), Tile(3, 4)) == False
    assert TileRect(Tile(3, 3), Tile(3, 3)).is_intersected_by(Tile(1, 3), Tile(4, 3)) == False
    assert TileRect(Tile(2, 3), Tile(5, 3)).is_intersected_by(Tile(3, 1), Tile(3, 5)) == False
    assert TileRect(Tile(3, 2), Tile(3, 5)).is_intersected_by(Tile(1, 3), Tile(5, 3)) == False
