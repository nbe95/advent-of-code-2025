def get_max_num(value: str, digits: int) -> int:
    # Exhaustive brute-force solution - works, but too slow for large num of digits
    if digits == 1 or len(value) == 1:
        return max(map(int, value))

    return max(
        int(value[index] + str(get_max_num(value[index + 1 :], digits - 1)))
        for index in range(len(value) - 1)
    )
