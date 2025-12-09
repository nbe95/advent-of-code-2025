from op_matrix import OpMatrix, OpMatrixRtl

input_str: list[str] = ["123 328  51 64 ", " 45 64  387 23 ", "  6 98  215 314", "*   +   *   +"]


def test_op_matrix() -> None:
    matrix = OpMatrix(input_str)
    assert matrix.calc_cols() == [33210, 490, 4243455, 401]
    assert matrix.get_grand_total() == 4277556


def test_op_matrix_rtl() -> None:
    matrix = OpMatrixRtl(input_str)
    assert matrix.calc_cols() == [8544, 625, 3253600, 1058]
    assert matrix.get_grand_total() == 3263827
