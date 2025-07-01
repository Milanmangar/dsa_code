# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/


# class Solution1:
#     def maximumSubarraySum(self, nums, k):
#         result = 0
#         for i in range(len(nums) - (k - 1)):
#             vals = nums[i : i + k]
#             if len(set(vals)) == k:
#                 result = max(result, sum(vals))
#         return result


class Solution:
    def maximumSubarraySum(self, nums, k):
        result = 0
        k_sum = 0
        seen = {}
        for i in range(k):
            curr_val = nums[i]
            k_sum += curr_val
            seen[curr_val] = seen.get(curr_val, 0) + 1
        if len(seen) == k:
            result = k_sum
        for i in range(k, len(nums)):
            left_pointer_val = nums[i - k]
            right_pointer_val = nums[i]
            k_sum = (k_sum - left_pointer_val) + right_pointer_val
            seen[left_pointer_val] -= 1
            if seen[left_pointer_val] == 0:
                del seen[left_pointer_val]
            seen[right_pointer_val] = seen.get(right_pointer_val, 0) + 1
            if len(seen) == k:
                result = max(result, k_sum)
        return result


# num2 = [1, 2, 3, 3, 4, 5]
# num2 = [1, 5, 4, 2, 9, 9, 9]
# num2 = [4, 4, 4]
num2 = [1, 5, 9, 9, 9, 4, 2, 8]
# num2 = [1, 2, 3, 3, 4]
k2 = 3
print(Solution().maximumSubarraySum(num2, k2))
