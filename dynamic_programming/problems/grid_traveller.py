# https://www.youtube.com/watch?v=oBt53YbR9Kk

travelled_grid = {}


def grid_traveller_normal(m, n):
    """brute force normal recursion time = 0(2^n), space = O(n^2)"""
    if m == 0 or n == 0:
        return 0
    if m == 1 and n == 1:
        return 1
    return grid_traveller_normal(m - 1, n) + grid_traveller_normal(m, n - 1)


# def grid_traveller_recur_dp(m, n):
#     """optimized recursive with memoization, time and space both are O(n^2)"""
#     visited_grid = f"{m}, {n}" if m > n else f"{n}, {m}"
#     if visited_grid in travelled_grid:
#         return travelled_grid[visited_grid]
#     if m == 0 or n == 0:
#         return 0
#     if m == 1 and n == 1:
#         return 1
#     travelled_grid[visited_grid] = grid_traveller_recur_dp(
#         m - 1, n
#     ) + grid_traveller_recur_dp(m, n - 1)
#     return travelled_grid[visited_grid]


def grid_traveller_table_dp(m, n):
    """Optimized with tabular, time and space both are O(n^2)"""
    table = [[0] * (n + 1) for _ in range(m + 1)]
    table[1][1] = 1
    for i in range(m + 1):
        for j in range(n + 1):
            curr_val = table[i][j]
            if j < n:
                table[i][j + 1] += curr_val
            if i < m:
                table[i + 1][j] += curr_val
    return table[m][n]


# print(grid_traveller_normal(2, 3))  # 3
# print(grid_traveller_normal(3, 3))  # 6
# print(grid_traveller_normal(5, 8))  # 330
# print(grid_traveller_normal(10, 10))  # 48620
# print(grid_traveller_normal(15, 15))  # 40116600

# print(grid_traveller_recur_dp(2, 3))  # 3
# print(grid_traveller_recur_dp(3, 3))  # 6
# print(grid_traveller_recur_dp(5, 8))  # 330
# print(grid_traveller_recur_dp(10, 10))  # 48620
# print(grid_traveller_recur_dp(15, 15))  # 40116600
# print(grid_traveller_recur_dp(18, 18))  # 2333606220

print(grid_traveller_table_dp(2, 3))  # 3
print(grid_traveller_table_dp(3, 3))  # 6
print(grid_traveller_table_dp(5, 8))  # 330
print(grid_traveller_table_dp(10, 10))  # 48620
print(grid_traveller_table_dp(15, 15))  # 40116600
print(grid_traveller_table_dp(18, 18))  # 2333606220
