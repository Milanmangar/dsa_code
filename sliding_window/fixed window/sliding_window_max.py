from collections import deque


class Solution:
    # def maxSlidingWindow(self, arr, k):
    #     """
    #     brute force
    #     Time: O(n * k)
    #         n = len(arr)
    #         k = sub array size
    #     Space: O(n)
    #     """
    #     result = []
    #     for i in range((len(arr) - k) + 1):
    #         max_val = arr[i]
    #         for j in range(i, (i + k)):
    #             max_val = max(max_val, arr[j])
    #         result.append(max_val)
    #     return result

    def maxSlidingWindow(self, arr, k):
        """
        optimized with sliding window with append
        Time: O(n)
            n = len(arr)
            k = sub array size
        Space: O(n)
        """
        result = []
        q = deque()
        q.append(0)
        for i in range(1, k):
            while len(q) > 0 and arr[i] > arr[q[-1]]:
                q.pop()
            q.append(i)

        result.append(arr[q[0]])
        for i in range(1, (len(arr) - k) + 1):
            coming_into_window = (i + k) - 1
            while len(q) > 0 and arr[coming_into_window] > arr[q[-1]]:
                q.pop()
            q.append(coming_into_window)
            if i > q[0]:
                q.popleft()
            result.append(arr[q[0]])
        return result

    # def maxSlidingWindow(self, arr, k):
    #     """
    #     optimized with sliding window with index insertion
    #     Time: O(n)
    #         n = len(arr)
    #         k = sub array size
    #     Space: O(n)
    #     """
    #     result = [0] * ((len(arr) - k) + 1)
    #     q = deque()
    #     q.append(0)
    #     for i in range(1, k):
    #         while len(q) > 0 and arr[i] > arr[q[-1]]:
    #             q.pop()
    #         q.append(i)

    #     result[0] = arr[q[0]]
    #     for i in range(1, (len(arr) - k) + 1):
    #         coming_into_window = (i + k) - 1
    #         while len(q) > 0 and arr[coming_into_window] > arr[q[-1]]:
    #             q.pop()
    #         q.append(coming_into_window)
    #         if i > q[0]:
    #             q.popleft()
    #         result[i] = arr[q[0]]
    #     return result


s = Solution()
print(s.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3))  # [3, 3, 5, 5, 6, 7]
print(
    s.maxSlidingWindow([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 2)
)  # [10, 9, 8, 7, 6, 5, 4, 3, 2]
print(s.maxSlidingWindow([1, -1], 1))  # [1,-1]
