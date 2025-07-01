# https://leetcode.com/problems/edit-distance/description/


class Solution:
    # def minDistance(self, s1, s2):
    #     """
    #     recursive brute force
    #     Time: O(3 ^ n + m)
    #         n=len(s1), m=len(s2)
    #     Space: O(n + m)
    #     """

    #     def answer(s1_index, s2_index):
    #         if s1_index >= len(s1):
    #             return len(s2) - s2_index
    #         if s2_index >= len(s2):
    #             return len(s1) - s1_index
    #         if s1[s1_index] == s2[s2_index]:
    #             return answer(s1_index + 1, s2_index + 1)
    #         insertion = 1 + answer(s1_index, s2_index + 1)
    #         deletion = 1 + answer(s1_index + 1, s2_index)
    #         replace = 1 + answer(s1_index + 1, s2_index + 1)
    #         return min(insertion, deletion, replace)

    #     return answer(0, 0)

    # def minDistance(self, s1, s2):
    #     """
    #     optimized recursive with memo
    #     Time: O(n * m)
    #         n=len(s1), m=len(s2)
    #     Space: O(n * m)
    #     """

    #     def answer(s1_index, s2_index, memo):
    #         if s1_index >= len(s1):
    #             return len(s2) - s2_index
    #         if s2_index >= len(s2):
    #             return len(s1) - s1_index
    #         if memo[s1_index][s2_index] != -1:
    #             return memo[s1_index][s2_index]
    #         if s1[s1_index] == s2[s2_index]:
    #             memo[s1_index][s2_index] = answer(s1_index + 1, s2_index + 1, memo)
    #             return memo[s1_index][s2_index]
    #         insertion = 1 + answer(s1_index, s2_index + 1, memo)
    #         deletion = 1 + answer(s1_index + 1, s2_index, memo)
    #         replace = 1 + answer(s1_index + 1, s2_index + 1, memo)
    #         memo[s1_index][s2_index] = min(insertion, deletion, replace)
    #         return memo[s1_index][s2_index]

    #     memo = [[-1] * len(s2) for _ in range(len(s1))]
    #     return answer(0, 0, memo)

    # def minDistance(self, s1, s2):
    #     """
    #     Tabular approach 2D
    #     Time: O(n * m)
    #         n=len(s1), m=len(s2)
    #     Space: O(n * m)
    #     """

    #     m, n = len(s1), len(s2)
    #     table = [[0] * (n + 1) for _ in range(m + 1)]
    #     table[0] = [i for i in range(n + 1)]
    #     for i in range(m + 1):
    #         table[i][0] = i

    #     for i in range(1, m + 1):
    #         for j in range(1, n + 1):
    #             if s1[i - 1] == s2[j - 1]:
    #                 table[i][j] = table[i - 1][j - 1]
    #             else:
    #                 insertion = 1 + table[i][j - 1]
    #                 deletion = 1 + table[i - 1][j]
    #                 replacement = 1 + table[i - 1][j - 1]
    #                 table[i][j] = min(insertion, deletion, replacement)

    #     return table[m][n]

    def minDistance(self, s1, s2):
        """
        Tabular approach 1D
        Time: O(n * m)
            n=len(s1), m=len(s2)
        Space: O(n * m)
        """

        m, n = len(s1), len(s2)
        prev = [i for i in range(n + 1)]

        for i in range(1, m + 1):
            curr = [0] * (n + 1)
            curr[0] = i
            for j in range(1, n + 1):
                if s1[i - 1] == s2[j - 1]:
                    curr[j] = prev[j - 1]
                else:
                    insertion = 1 + curr[j - 1]
                    deletion = 1 + prev[j]
                    replacement = 1 + prev[j - 1]
                    curr[j] = min(insertion, deletion, replacement)
            prev = curr

        return prev[n]


s = Solution()
print(s.minDistance("horse", "ros"))  # 3
print(s.minDistance("intention", "execution"))  # 5
