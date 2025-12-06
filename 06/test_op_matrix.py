from op_matrix import OpMatrix, OpMatrixRtl


def test_op_matrix() -> None:
    m = OpMatrix(["123 328  51 64 ", " 45 64  387 23 ", "  6 98  215 314", "*   +   *   +"])
    assert m.calc_cols() == [33210, 490, 4243455, 401]
    assert m.get_grand_total() == 4277556


def test_op_matrix_rtl() -> None:
    m = OpMatrixRtl(["123 328  51 64 ", " 45 64  387 23 ", "  6 98  215 314", "*   +   *   +"])
    assert m.calc_cols() == [8544, 625, 3253600, 1058]
    assert m.get_grand_total() == 3263827
