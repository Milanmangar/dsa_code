# https://leetcode.com/problems/decode-ways/


class Solution:
    # def numDecodings(self, s: str) -> int:
    #     """
    #     recusive brute force
    #     Time: O(2^n)
    #         n = length of s
    #     Space: O(n)
    #     """

    #     def answer(index):
    #         if index == len(s):
    #             return 1
    #         if s[index] == "0":
    #             return 0

    #         # print(index)
    #         val = answer(index + 1)
    #         if index < len(s) - 1 and (
    #             s[index] == "1" or s[index] == "2" and int(s[index + 1]) < 7
    #         ):
    #             val += answer(index + 2)
    #         return val

    #     return answer(0)

    # def numDecodings(self, s: str) -> int:
    #     """
    #     optimized recusive with memoization
    #     Time: O(n)
    #         n = length of s
    #     Space: O(n)
    #     """

    #     def answer(index, memo):
    #         if index == len(s):
    #             return 1
    #         if s[index] == "0":
    #             return 0
    #         if memo[index] != -1:
    #             return memo[index]

    #         # print(index)
    #         val = answer(index + 1, memo)
    #         if index < len(s) - 1 and (10 <= int(s[index : index + 2]) <= 26):
    #             val += answer(index + 2, memo)
    #         memo[index] = val
    #         return memo[index]

    #     memo = [-1] * (len(s) + 1)
    #     return answer(0, memo)

    def numDecodings(self, s: str) -> int:
        """
        tabular approach
        Time: O(n)
            n = length of s
        Space: O(n)
        """

        table = [0] * (len(s) + 1)
        table[0] = 1
        table[1] = 1 if s[0] != "0" else 0
        for i in range(2, len(s) + 1):
            single_digit = table[i - 1] if s[i - 1] != "0" else 0
            double_digit = table[i - 2] if (10 <= int(s[i - 2 : i]) <= 26) else 0
            table[i] = single_digit + double_digit

        return table[len(s)]

    def numDecodings(self, s: str) -> int:
        """
        tabular approach
        Time: O(n)
            n = length of s
        Space: O(1)
        """

        second_from_curr_index = 1
        first_from_curr_index = 1 if s[0] != "0" else 0
        for i in range(2, len(s) + 1):
            single_digit = first_from_curr_index if s[i - 1] != "0" else 0
            double_digit = (
                second_from_curr_index if (10 <= int(s[i - 2 : i]) <= 26) else 0
            )
            second_from_curr_index = first_from_curr_index
            first_from_curr_index = single_digit + double_digit

        return first_from_curr_index


s = Solution()
# print(s.numDecodings("1023"))  # 0
print(s.numDecodings("12"))  # 2
print(s.numDecodings("226"))  # 3
print(s.numDecodings("11106"))  # 2
print(s.numDecodings("27"))  # 1
