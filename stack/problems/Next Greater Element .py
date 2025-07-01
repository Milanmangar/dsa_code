# https://www.geeksforgeeks.org/next-greater-element/


# class Solution:
#     # Time: 0(1)
#     # Space: 0(n^2)
#     def nextGreaterElements(self, nums):

#         for i in range(len(nums)):
#             is_greater_exists = False
#             for j in range(i + 1, len(nums)):
#                 if nums[j] > nums[i]:
#                     nums[i] = nums[j]
#                     is_greater_exists = True
#                     break
#             if not is_greater_exists:
#                 nums[i] = -1
#         return nums


# class Solution:
#     # Time: 0(1)
#     # Space: 0(n)
#     def nextGreaterElements(self, nums):
#         left = 0
#         right = 1
#         while left < len(nums) - 1:
#             if nums[right] > nums[left]:
#                 nums[left] = nums[right]
#                 left += 1
#                 right = left + 1

#             elif right >= len(nums) - 1:
#                 nums[left] = -1
#                 left += 1
#                 right = left + 1
#             else:
#                 right += 1
#         nums[-1] = -1
#         return nums


class Solution:
    # Time: 0(1)
    # Space: 0(n^2)
    def nextGreaterElements(self, nums):
        stack = []
        i = actual_len = len(nums) - 1
        while i >= 0:
            correct_index = actual_len - i
            if len(stack) == 0:
                stack.append(nums[i])
                nums[i] = -1
            elif stack[-1] > nums[i]:
                top_val = stack[-1]
                stack.append(nums[i])
                nums[i] = top_val
            else:
                while len(stack) > 0:
                    poped_nums = stack.pop()
                    if poped_nums > nums[i]:
                        stack.append(nums[i])
                        nums[i] = poped_nums
                        break
                if len(stack) == 0:
                    nums[i] = -1
            i -= 1
        return nums


# nums = [4, 5, 2, 25]  # output = [5, 25, 25, -1]

nums = [13, 7, 6, 12]  # output = [-1, 12, 12, -1]

# nums = [1, 3, 2, 4]  # output = [3, 4, 4, -1]

# nums = [1, 3, 0, 0, 1, 2, 4]  # output = [3, 4, 1, 1, 2, 4, -1]
print(Solution().nextGreaterElements(nums))
