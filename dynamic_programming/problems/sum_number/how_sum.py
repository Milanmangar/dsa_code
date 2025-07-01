# https://www.youtube.com/watch?v=oBt53YbR9Kk


# def how_sum_recur(target: int, numbers: list) -> bool:
#     """normal brute force recursive, time = O(n^m * m) -> exponential, space = O(m) -> linear"""
#     if target == 0:
#         return []
#     if target < 0:
#         return None
#     for num in numbers:
#         remainder = target - num
#         remainder_result = how_sum_recur(remainder, numbers)
#         if remainder_result is not None:
#             return remainder_result + [num]
#     return None


# print(how_sum_recur(7, [2, 3]))  # [3, 2, 2]
# print(how_sum_recur(7, [2, 4, 6]))  # None
# print(how_sum_recur(7, [5, 3, 4, 7]))  # [4, 3]
# print(how_sum_recur(7, [2, 4]))  # None
# print(how_sum_recur(300, [7, 14]))  # False


# def how_sum_recur_memoization(target: int, numbers: list, memo: dict) -> bool:
#     """Optimized recursive with memoization, time= O(mn*m^2), space= O(m^2)"""
#     if target in memo:
#         return memo[target]
#     if target == 0:
#         return []
#     if target < 0:
#         return None
#     for num in numbers:
#         remainder = target - num
#         remainder_result = how_sum_recur_memoization(remainder, numbers, memo)
#         if remainder_result is not None:
#             memo[target] = remainder_result + [num]
#             return memo[target]
#             # return True
#     memo[target] = None
#     return None


# print(how_sum_recur_memoization(7, [2, 3], {}))  # [3, 2, 2]
# print(how_sum_recur_memoization(7, [2, 4, 6], {}))  # None
# print(how_sum_recur_memoization(7, [5, 3, 4, 7], {}))  # [4, 3]
# print(how_sum_recur_memoization(7, [2, 4], {}))  # None
# print(how_sum_recur_memoization(8, [2, 3, 5], {}))  # [2, 2, 2, 2]
# print(how_sum_recur_memoization(300, [7, 14], {}))  # None


# def how_sum_table(target: int, numbers: list) -> bool:
#     """Optimized recursive with memoization, time= O(n * m), space= O(n) but
#     You lose the actual structure of the combination (e.g., can't recover [2, 3, 2] easily from 232)
#     It assumes all num are single-digit for accurate encoding; otherwise, digit-wise logic may break
#     """
#     table = [None for _ in range(target + 1)]
#     table[0] = 0
#     for i in range(target):
#         if table[i] is not None:
#             for num in numbers:
#                 if (i + num) <= target:
#                     table[i + num] = (table[i] * 10) + num
#     # print(table)
#     return table[target]


def how_sum_table(target: int, numbers: list) -> bool:
    """Optimized recursive with memoization, time= O(mn*m^2), space= O(m^2)"""
    table = [None for _ in range(target + 1)]
    table[0] = []
    for i in range(target):
        if table[i] is not None:
            for num in numbers:
                if (i + num) <= target:
                    table[i + num] = table[i] + [num]
    # print(table)
    return table[target]


print(how_sum_table(7, [2, 3]))  # [3, 2, 2]
print(how_sum_table(7, [2, 4, 6]))  # None
print(how_sum_table(7, [5, 3, 4, 7]))  # [4, 3]
print(how_sum_table(7, [2, 4]))  # None
print(how_sum_table(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(how_sum_table(300, [7, 14]))  # None
print(how_sum_table(22, [11, 20, 2]))  # None
