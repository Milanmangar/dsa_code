# https://leetcode.com/problems/shortest-common-supersequence/description/


class Solution:
    # def shortestCommonSupersequence(self, s1, s2):
    #     """
    #     recursive brute force
    #     Time: O(2 ^ n + m)
    #         n=len(s1), m=len(s2)
    #     Space: O(n + m)
    #     """

    #     def answer(index_s1, index_s2):
    #         if index_s1 >= len(s1):
    #             return len(s2) - index_s2
    #         if index_s2 >= len(s2):
    #             return len(s1) - index_s1
    #         if s1[index_s1] == s2[index_s2]:
    #             return 1 + answer(index_s1 + 1, index_s2 + 1)
    #         c2 = 1 + answer(index_s1 + 1, index_s2)
    #         c3 = 1 + answer(index_s1, index_s2 + 1)
    #         return min(c2, c3)

    #     return answer(0, 0)

    # def shortestCommonSupersequence(self, s1, s2):
    #     """
    #     recursive brute force
    #     Time: O(n * m)
    #         n=len(s1), m=len(s2)
    #     Space: O(n * m)
    #     """

    #     def answer(index_s1, index_s2, memo):
    #         if index_s1 >= len(s1):
    #             return len(s2) - index_s2
    #         if index_s2 >= len(s2):
    #             return len(s1) - index_s1
    #         if memo[index_s1][index_s2] != -1:
    #             return memo[index_s1][index_s2]
    #         if s1[index_s1] == s2[index_s2]:
    #             memo[index_s1][index_s2] = 1 + answer(index_s1 + 1, index_s2 + 1, memo)
    #             return memo[index_s1][index_s2]
    #         c2 = 1 + answer(index_s1 + 1, index_s2, memo)
    #         c3 = 1 + answer(index_s1, index_s2 + 1, memo)
    #         memo[index_s1][index_s2] = min(c2, c3)
    #         return memo[index_s1][index_s2]

    #     memo = [[-1] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    #     return answer(0, 0, memo)

    # def shortestCommonSupersequence(self, s1, s2):
    #     """
    #     Tabular 2D
    #     Time: O(n * m)
    #         n=len(s1), m=len(s2)
    #     Space: O(n * m)
    #     """

    #     n, m = (len(s1) + 1), (len(s2) + 1)
    #     table = [[0] * (m) for _ in range(n)]
    #     table[0] = [i for i in range(m)]
    #     for i in range(n):
    #         table[i][0] = i

    #     for i in range(1, n):
    #         for j in range(1, m):
    #             if s1[i - 1] == s2[j - 1]:
    #                 table[i][j] = 1 + table[i - 1][j - 1]
    #             else:
    #                 exclude_s1 = 1 + table[i - 1][j]
    #                 exclude_s2 = 1 + table[i][j - 1]
    #                 table[i][j] = min(exclude_s1, exclude_s2)
    #     return table[n - 1][m - 1]

    def shortestCommonSupersequence(self, s1, s2):
        """
        Tabular 1D
        Time: O(n * m)
            n=len(s1), m=len(s2)
        Space: O(m)
        """

        n, m = (len(s1) + 1), (len(s2) + 1)
        table = [i for i in range(m)]

        for i in range(1, n):
            curr_table = [0] * m
            curr_table[0] = i
            for j in range(1, m):
                if s1[i - 1] == s2[j - 1]:
                    curr_table[j] = 1 + table[j - 1]
                else:
                    exclude_s1 = 1 + table[j]
                    exclude_s2 = 1 + curr_table[j - 1]
                    curr_table[j] = min(exclude_s1, exclude_s2)
            table = curr_table

        return table[m - 1]


s = Solution()
print(s.shortestCommonSupersequence("abac", "cab"))  # 5
print(s.shortestCommonSupersequence("aaaaaaaa", "aaaaaaaa"))  # 8
print(s.shortestCommonSupersequence("geek", "eke"))  # 5
print(s.shortestCommonSupersequence("AGGTAB", "GXTXAYB"))  # 9
print(s.shortestCommonSupersequence("geek", "ek"))  # 4
