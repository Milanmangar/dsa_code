class Solution:
    # def search(self, pat, text):
    #     """
    #     brute force
    #     Time: O(n * k)
    #         n = len(text)
    #         k = len(pat)
    #     Space: O(n)
    #     """
    #     letter_count = {}
    #     for i in pat:
    #         if i in letter_count:
    #             letter_count[i] += 1
    #         else:
    #             letter_count[i] = 1

    #     result = 0

    #     for i in range((len(text) - len(pat)) + 1):
    #         temp_dict = {}
    #         for j in range(i, i + len(pat)):
    #             if text[j] in temp_dict:
    #                 temp_dict[text[j]] += 1
    #             else:
    #                 temp_dict[text[j]] = 1
    #         if temp_dict == letter_count:
    #             result += 1
    #     return result

    def search(self, pat, text):
        """
        optimized with sliding window
        Time: O(n)
            n = len(text)
            k = len(pat)
        Space: O(n)
        """
        # a-z letter generation
        letter_count = {chr(letter): 0 for letter in range(97, 97 + 26)}
        for i in pat:
            letter_count[i] += 1

        l_text = len(text)
        l_pat = len(pat)
        # a-z letter generation
        temp_letter_count = {chr(letter): 0 for letter in range(97, 97 + 26)}
        for i in range(l_pat):
            temp_letter_count[text[i]] += 1

        result = 1 if temp_letter_count == letter_count else 0
        for i in range(1, ((l_text - l_pat) + 1)):
            going_out_of_window = text[i - 1]
            coming_into_window = text[(i + l_pat) - 1]
            temp_letter_count[going_out_of_window] -= 1
            temp_letter_count[coming_into_window] += 1

            if letter_count == temp_letter_count:
                result += 1

        return result


s = Solution()
print(s.search("for", "forxxorfxdofr"))  # 3
print(s.search("aaba", "aabaabaa"))  # 4
