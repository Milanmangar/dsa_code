# https://www.youtube.com/watch?v=oBt53YbR9Kk


# def best_sum_recur(target: int, numbers: list) -> int:
#     """normal brute force recursive, time = O(n^m * m) -> exponential, space = O(m^2)"""
#     if target == 0:
#         return []
#     if target < 0:
#         return None
#     best_combination = None

#     for num in numbers:
#         remainder = target - num
#         curr_combination = best_sum_recur(remainder, numbers)
#         if curr_combination is not None:
#             curr_combination = curr_combination + [num]
#             if best_combination is None or len(curr_combination) < len(
#                 best_combination
#             ):
#                 best_combination = curr_combination
#     return best_combination


# print(best_sum_recur(3, [2, 1, 3]))  # [5, 3]
# print(best_sum_recur(8, [2, 3, 5]))  # [5, 3]
# print(best_sum_recur(8, [1, 4, 5]))  # [4, 4]
# # print(best_sum_recur(100, [1, 2, 5, 25]))  # [5, 3]


# def best_sum_recur_memoization(target: int, numbers: list, memo: dict) -> int:
#     """Optimized recursive with memoization, time= O(m^2n), space= O(m^2)"""
#     if target in memo:
#         return memo[target]
#     if target == 0:
#         return []
#     if target < 0:
#         return None
#     best_combination = None

#     for num in numbers:
#         remainder = target - num
#         curr_combination = best_sum_recur_memoization(remainder, numbers, memo)
#         if curr_combination is not None:
#             curr_combination = curr_combination + [num]
#             if best_combination is None or len(curr_combination) < len(
#                 best_combination
#             ):
#                 best_combination = curr_combination
#     memo[target] = best_combination
#     return best_combination


# print(best_sum_recur_memoization(3, [2, 1, 3], {}))  # [5, 3]
# print(best_sum_recur_memoization(8, [2, 3, 5], {}))  # [5, 3]
# print(best_sum_recur_memoization(8, [1, 4, 5], {}))  # [4, 4]
# print(best_sum_recur_memoization(100, [1, 2, 5, 25], {}))  # [25, 25, 25, 25]


def best_sum_table(target: int, numbers: list) -> bool:
    """Optimized  with table, time= O(mn*m^2), space= O(m^2)"""
    table = [None for _ in range(target + 1)]
    table[0] = []
    for i in range(target):
        if table[i] is not None:
            for num in numbers:
                if (i + num) <= target:
                    if (table[i + num] is None) or (
                        len(table[i] + [num]) < len(table[i + num])
                    ):
                        table[i + num] = table[i] + [num]
    return table[target]


print(best_sum_table(3, [2, 1, 3]))  # [3]
print(best_sum_table(8, [2, 3, 5]))  # [3, 5]
print(best_sum_table(8, [1, 4, 5]))  # [4, 4]
print(best_sum_table(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
