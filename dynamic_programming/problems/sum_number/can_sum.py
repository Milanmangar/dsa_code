# https://www.youtube.com/watch?v=oBt53YbR9Kk


# def can_sum_recur(target: int, numbers: list) -> bool:
#     """normal brute force recursive, time = O(n^m) -> exponential, space = O(m) -> linear"""
#     if target == 0:
#         return True
#     if target < 0:
#         return False
#     for num in numbers:
#         remainder = target - num
#         if can_sum_recur(remainder, numbers) is True:
#             return True
#     return False


# def can_sum_recur_memoization(target: int, numbers: list, memo: dict) -> bool:
#     """Optimized recursive with memoization, time= O(m*n) -> n^2, space= O(n)"""
#     if target in memo:
#         return memo[target]
#     if target == 0:
#         return True
#     if target < 0:
#         return False
#     for num in numbers:
#         remainder = target - num
#         if can_sum_recur_memoization(remainder, numbers, memo):
#             memo[target] = True
#             return True
#     memo[target] = False
#     return False


def can_sum_table(target: int, numbers: list) -> bool:
    """Optimized using table, time= O(m*n) -> n^2, space= O(n)"""
    table = [False for _ in range(target + 1)]
    table[0] = True
    for i in range(target):
        if table[i] == True:
            for num in numbers:
                if (i + num) <= target:
                    table[i + num] = True
    # print(table)
    return table[target]


# print(can_sum_recur(7, [2, 3]))  # True
# print(can_sum_recur(7, [2, 4, 6]))  # False
# print(can_sum_recur(7, [5, 3, 4, 7]))  # True
# print(can_sum_recur(7, [2, 4]))  # False
# print(can_sum_recur(300, [7, 14]))  # False


# print(can_sum_recur_memoization(7, [2, 3], {}))  # True
# print(can_sum_recur_memoization(7, [2, 4, 6], {}))  # False
# print(can_sum_recur_memoization(7, [5, 3, 4, 7], {}))  # True
# print(can_sum_recur_memoization(7, [2, 4], {}))  # False
# print(can_sum_recur_memoization(300, [7, 14], {}))  # False

print(can_sum_table(7, [2, 3]))  # True
print(can_sum_table(7, [2, 4, 6]))  # False
print(can_sum_table(7, [5, 3, 4, 7]))  # True
print(can_sum_table(7, [2, 4]))  # False
print(can_sum_table(300, [7, 14]))  # False
