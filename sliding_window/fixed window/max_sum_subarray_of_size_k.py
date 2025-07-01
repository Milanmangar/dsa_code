# https://www.geeksforgeeks.org/problems/max-sum-subarray-of-size-k5313/1


class Solution:
    # def maximumSumSubarray(self, arr, k):
    #     """
    #     Brute force approch

    #     Time Complexity:
    #         O(n * k):
    #             n = len(arr).
    #             k = sub array size
    #         Explanation: For each starting index i, the inner loop sums k elements.

    #     Space Complexity:
    #         O(1)
    #     """
    #     max_sum = 0
    #     for i in range((len(arr) - k) + 1):
    #         curr_sum = 0
    #         for j in range(i, i + k):

    #             curr_sum += arr[j]
    #         max_sum = max(curr_sum, max_sum)
    #     return max_sum

    def maximumSumSubarray(self, arr, k):
        """
        optimized with sliding window
        Time Complexity:
            O(n):
                n = len(arr).
            Explanation: For each starting index i, the inner loop sums k elements.

        Space Complexity:
            O(1)
        """
        max_sum = sum(arr[:k])
        curr_sum = max_sum
        for i in range(k, len(arr)):
            curr_sum = (curr_sum - arr[i - k]) + arr[i]
            max_sum = max(curr_sum, max_sum)
        return max_sum


s = Solution()
# print(s.maximumSumSubarray([100, 200, 300, 400], 2))  # 700
# print(s.maximumSumSubarray([100, 200, 300, 400], 4))  # 1000
# print(s.maximumSumSubarray([100, 200, 300, 400], 1))  # 400
print(
    s.maximumSumSubarray([9479, 488, 2374, 1583, 5863, 7811, 6916, 1685, 3960], 5)
)  # 26235
