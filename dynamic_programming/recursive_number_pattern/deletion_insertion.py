# http://geeksforgeeks.org/problems/minimum-number-of-deletions-and-insertions0209/1


class Solution:
    # def minOperations(self, s1, s2):
    #     """
    #     recursive brute force
    #     Time: O(2 ^ n + m)
    #         n=len(s1), m=len(s2)
    #     Space: O(n + m)
    #     """

    #     def answer(s1_index, s2_index):
    #         if s1_index >= len(s1) or s2_index >= len(s2):
    #             return 0
    #         c1 = 0
    #         if s1[s1_index] == s2[s2_index]:
    #             c1 = 1 + answer(s1_index + 1, s2_index + 1)
    #         c2 = answer(s1_index + 1, s2_index)
    #         c3 = answer(s1_index, s2_index + 1)

    #         return max(c1, c2, c3)

    #     result = answer(0, 0)
    #     result = (len(s1) - result) + (len(s2) - result)
    #     return result

    # def minOperations(self, s1, s2):
    #     """
    #     optmized recursive with memoization
    #     Time: O(n * m)
    #         n=len(s1), m=len(s2)
    #     Space: O(n * m)
    #     """

    #     def answer(s1_index, s2_index, memo):
    #         if memo[s1_index][s2_index] != -1:
    #             return memo[s1_index][s2_index]
    #         if s1_index >= len(s1) or s2_index >= len(s2):
    #             return 0
    #         c1 = 0
    #         if s1[s1_index] == s2[s2_index]:
    #             c1 = 1 + answer(s1_index + 1, s2_index + 1, memo)
    #         c2 = answer(s1_index + 1, s2_index, memo)
    #         c3 = answer(s1_index, s2_index + 1, memo)
    #         memo[s1_index][s2_index] = max(c1, c2, c3)
    #         return memo[s1_index][s2_index]

    #     memo = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    #     result = answer(0, 0, memo)
    #     result = (len(s1) - result) + (len(s2) - result)
    #     return result

    # def minOperations(self, s1, s2):
    #     """
    #     tabular 2D
    #     Time: O(n * m)
    #         n=len(s1), m=len(s2)
    #     Space: O(n * m)
    #     """
    #     m, n = len(s1), len(s2)
    #     table = [[0] * (n + 1) for _ in range(m + 1)]
    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             if s1[i - 1] == s2[j - 1]:
    #                 table[i][j] = 1 + table[i - 1][j - 1]
    #             else:
    #                 skip_left = table[i - 1][j]
    #                 skip_right = table[i][j - 1]
    #                 table[i][j] = max(skip_left, skip_right)

    #     result = table[m][n]
    #     result = (m - result) + (n - result)
    #     return result

    def minOperations(self, s1, s2):
        """
        tabular 1D
        Time: O(n * m)
            n=len(s1), m=len(s2)
        Space: O(m)
        """
        m, n = len(s1), len(s2)
        prev_table = [0] * (n + 1)
        for i in range(1, m + 1):
            curr_table = [0] * (n + 1)
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr_table[j] = 1 + prev_table[j - 1]
                else:
                    skip_left = prev_table[j]
                    skip_right = curr_table[j - 1]
                    curr_table[j] = max(skip_left, skip_right)
            prev_table = curr_table

        result = prev_table[n]
        result = (m - result) + (n - result)
        return result


s = Solution()
print(s.minOperations("heap", "pea"))  # 3
print(s.minOperations("geeksforgeeks", "geeks"))  # 8
print(s.minOperations("horse", "ros"))  # 4
