# https://leetcode.com/problems/reverse-words-in-a-string/

# class Soluiton:
#     def reverseWords(self, s):
#         print(s)
#         l = list(s)

#         def reverse(left, right):
#             while left < right:
#                 temp = l[right]
#                 l[right] = l[left]
#                 l[left] = temp
#                 left += 1
#                 right -= 1

#         reverse(0, len(l) - 1)
#         left_pointer = 0
#         for right_pointer in range(len(l)):
#             if l[right_pointer] == " ":
#                 reverse(left_pointer, right_pointer - 1)
#                 left_pointer = right_pointer + 1
#         reverse(left_pointer, right_pointer)
#         return "".join(l)


# class Soluiton:
#     def reverseWords(self, s):
#         result = ""
#         word = ""
#         index = len(s) - 1
#         while index >= 0:
#             if s[index] == " ":
#                 result = result + f"{word} "
#                 word = ""
#             else:
#                 word = s[index] + word
#             index -= 1
#         result += word
#         return result


# class Soluiton:
#     def reverseWords(self, s):
#         print(s)
#         l = s.split(" ")
#         return " ".join(l[::-1])


# class Soluiton:
#     def reverseWords(self, s):
#         result = ""
#         word = ""
#         index = len(s) - 1
#         while index >= 0:
#             if s[index] == " ":
#                 result = result + f"{word} "
#                 word = ""
#             else:
#                 word = s[index] + word
#             index -= 1
#         result += word
#         return result

# solutions actual

# class Soluiton:
#     def reverseWords(self, s):
#         l = [letter for letter in s.split(" ") if letter and letter != " "]
#         return " ".join(l[::-1])


# class Soluiton:
#     def reverseWords(self, s):
#         result = ""
#         word = ""
#         index = len(s) - 1
#         while index >= 0:
#             if s[index] == " ":
#                 if word:
#                     result = result + f"{word} "
#                     word = ""
#             else:
#                 word = s[index] + word
#             index -= 1
#         result += word
#         if result[-1] == " ":
#             result = result[:-1]
#         return result


class Soluiton:
    def reverseWords(self, s):
        # print(s)
        l = list(s)

        def reverse(left, right):
            while left < right:
                temp = l[right]
                l[right] = l[left]
                l[left] = temp
                left += 1
                right -= 1

        reverse(0, len(l) - 1)
        left_pointer = 0
        for right_pointer in range(len(l)):
            if l[right_pointer] == " ":
                reverse(left_pointer, right_pointer - 1)
                left_pointer = right_pointer + 1
        reverse(left_pointer, right_pointer)
        space_count = 0
        for index in range(len(l) - 1):
            if l[index] == " ":
                space_count += 1
                if space_count < 2:
                    l[index] = True
                else:
                    l[index] = False
            else:
                space_count = 0
        if l[-1] == " ":
            l = l[:-1]
        l = [
            letter if type(letter) is not bool else " "
            for letter in l
            if (type(letter) is bool and letter) or type(letter) is not bool
        ]
        if l[0] == " ":
            l = l[1:]

        return "".join(l)


word = "a"
# print(word)
print(Soluiton().reverseWords(word))
