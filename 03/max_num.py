def get_max_num(value: str, digits: int) -> int:
    result: int = 0
    offset: int = 0
    for index in range(digits):
        # Look ahead `digits-index` positions (leaving enough digits to be taken by further iterations) and take biggest number occurring first
        candidates: str = value[offset : len(value) - (digits - index - 1)]
        max_digit: int = max(map(int, candidates))
        offset += candidates.find(str(max_digit)) + 1
        result = result * 10 + max_digit
    return result


def get_max_num_brute_force(value: str, digits: int) -> int:
    # Exhaustive brute-force solution - works, but too slow for large num of digits
    if digits == 1 or len(value) == 1:
        return max(map(int, value))

    return max(
        int(value[index] + str(get_max_num_brute_force(value[index + 1 :], digits - 1)))
        for index in range(len(value) - 1)
    )
