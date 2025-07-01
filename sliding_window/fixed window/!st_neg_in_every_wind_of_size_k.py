# User function Template for python3
# https://www.youtube.com/watch?v=Rot0y4cmlNw

from collections import deque


class Solution:
    # def firstNegInt(self, arr, k):
    #     """
    #     brute force
    #     Time: O(n * k)
    #         n = len(arr)
    #         k = sub array size
    #     Space: O(n)
    #     """

    #     result = []
    #     for i in range((len(arr) - k) + 1):
    #         has_negative = False
    #         for j in range(i, i + k):
    #             if arr[j] < 0:
    #                 result.append(arr[j])
    #                 has_negative = True
    #                 break
    #         if has_negative is False:
    #             result.append(0)
    #     return result

    def firstNegInt(self, arr, k):
        """
        optimized with silding window
        Time: O(n)
            n = len(arr)
            k = sub array size
        Space: O(n)
        """

        result = []
        q = deque()
        index = 0
        while index < k:
            if arr[index] < 0:
                q.append(arr[index])
            index += 1
        result.append(q[0] if len(q) > 0 else 0)

        for i in range(1, (len(arr) - k) + 1):
            if arr[i - 1] < 0:
                q.popleft()
            if arr[(i + k) - 1] < 0:
                q.append(arr[(i + k) - 1])

            result.append(q[0] if len(q) > 0 else 0)

        return result


s = Solution()
# print(s.firstNegInt([-8, 2, 3, -6, 10], 2))  # [-8, 0, -6, -6]
# print(s.firstNegInt([12, -1, -7, 8, -15, 30, 16, 28], 3))  # [-1, -1, -7, -15, -15, 0]
print(s.firstNegInt([12, 1, 3, 5], 3))  # [0, 0]
