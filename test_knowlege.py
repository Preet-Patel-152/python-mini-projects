def split_parity(nums: list[int]) -> dict[str, list[int]]:
    even = [num for num in nums if num % 2 == 0]
    odd = [num for num in nums if num % 2 != 0]
    return {"even": even, "odd": odd}
