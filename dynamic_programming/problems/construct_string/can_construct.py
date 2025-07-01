# https://www.youtube.com/watch?v=oBt53YbR9Kk

# def can_construct(target_word: str, word_list: list) -> bool:
#     """not working for not maintaining sequence"""
#     result = False
#     for word1 in word_list:
#         answer = ""
#         for word2 in word_list:
#             curr_word = word1 + word2
#             if target_word.startswith(curr_word):
#                 word1 = answer = curr_word
#                 # word1 = answer
#         if answer == target_word:
#             result = True
#             break
#     return result


# print(can_construct("skateboard", ["bo", "rd", "d", "te", "te", "ska", "sk", "board"]))
# print(can_construct("abcdef", ["ab", "ef", "abc", "ac", "d"]))


# def can_construct_recur(target_word: str, word_list: list) -> bool:
#     """normal brute force recursive, time = O(n^m * m) -> exponential, space = O(m^2)"""
#     if target_word == "":
#         return True

#     for word in word_list:
#         if target_word.startswith(word):
#             l = len(word)
#             remaining = target_word[l:]
#             if can_construct_recur(remaining, word_list):
#                 return True
#     return False


# print(can_construct_recur("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
# print(
#     can_construct_recur(
#         "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boards"]
#     )  # False
# )
# print(
#     can_construct_recur("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
# )  # True
# print(
#     can_construct_recur(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]
#     )
# )


# def can_construct_memoization(target_word: str, word_list: list, memo) -> bool:
#     """Optimized recursive with memoization, time= O(n*m^2) -> polynomial, space= O(m^2)"""
#     if target_word in memo:
#         return memo[target_word]
#     if target_word == "":
#         return True

#     for word in word_list:
#         if target_word.startswith(word):
#             l = len(word)
#             remaining = target_word[l:]
#             if can_construct_memoization(remaining, word_list, memo):
#                 memo[target_word] = True
#                 return True
#     memo[target_word] = False
#     return False


# print(
#     can_construct_memoization("abcdef", ["ab", "abc", "cd", "def", "abcd"], {})
# )  # True
# print(
#     can_construct_memoization(
#         "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boards"], {}
#     )  # False
# )
# print(
#     can_construct_memoization(
#         "enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}
#     )
# )  # True
# print(
#     can_construct_memoization(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"], {}
#     )
# )


def can_construct_table(target_word: str, word_list: list) -> bool:
    """Optimized  with table, time= O(n*m^2) -> polynomial, space= O(m^2)"""
    table = [False for _ in range(len(target_word) + 1)]
    table[0] = True

    for i in range(len(target_word)):
        if table[i] == True:
            for word in word_list:
                if (i + len(word)) <= len(target_word):
                    if target_word[i : i + len(word)] == word:
                        table[i + len(word)] = True
    return table[len(target_word)]


print(can_construct_table("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # True
print(
    can_construct_table(
        "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boards"]
    )  # False
)
print(
    can_construct_table("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
)  # True
print(
    can_construct_table(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]
    )
)  # False
