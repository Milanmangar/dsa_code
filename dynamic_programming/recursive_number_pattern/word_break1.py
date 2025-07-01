# https://leetcode.com/problems/word-break/submissions/1675896406/
# https://www.youtube.com/watch?v=hK6Git1o42c


class Solution:
    # def wordBreak(self, s: str, wordDict: list[str]) -> bool:
    #     """
    #     recursive brute force
    #     Time: O(2ⁿ)
    #         n = length of string s
    #         k = average number of dictionary words that match substrings starting at a given index (can vary)
    #     Space: O(n)
    #     """
    #     len_s = len(s)
    #     wordDict = set(wordDict)
    #     if s in wordDict:
    #         return True

    #     def answer(start):
    #         if start == len_s:
    #             return True
    #         for end in range(start + 1, (len_s + 1)):
    #             if s[start:end] in wordDict and answer(end):
    #                 return True
    #         return False

    #     return answer(0)

    # def wordBreak(self, s: str, wordDict: list[str]) -> bool:
    #     """
    #     optimized recursive with memoization
    #     Time: O(n * k)
    #         n = length of string s
    #         k = average number of dictionary words that match substrings starting at a given index (can vary)
    #     Space: O(n)
    #     """
    #     len_s = len(s)
    #     wordDict = set(wordDict)
    #     if s in wordDict:
    #         return True

    #     def answer(start, memo):
    #         if start == len_s:
    #             return True
    #         if memo[start] != -1:
    #             return memo[start]
    #         for end in range(start + 1, (len_s + 1)):
    #             if s[start:end] in wordDict and answer(end, memo):
    #                 memo[start] = True
    #                 return True
    #         memo[start] = False
    #         return False

    #     memo = [-1] * (len_s + 1)
    #     return answer(0, memo)

    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        """
        Bottom-up DP with 1D table and max word length optimization.
        Time: O(n * k)
            n = length of string s
            k = max length of words in the dictionary
        Space: O(n)
        """
        wordDict = set(wordDict)
        max_word_len = max(map(len, wordDict))
        n = len(s)
        table = [False] * (n + 1)
        table[0] = True  # empty string is always "breakable"

        for i in range(1, n + 1):
            for j in range(max(0, i - max_word_len), i):
                if table[j] and s[j:i] in wordDict:
                    table[i] = True
                    break  # no need to check further if one valid segmentation is found

        return table[n]


s = Solution()
print(s.wordBreak("leetcode", ["leet", "code"]))  # True
print(s.wordBreak("applepenapple", ["apple", "pen"]))  # True
print(s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))  # False
print(s.wordBreak("cars", ["car", "ca", "rs"]))  # True
