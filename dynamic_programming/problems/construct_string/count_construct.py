# def count_construct_recur(target_word: str, word_list: list) -> bool:
#     """normal brute force recursive, time = O(n^m * m) -> exponential, space = O(m^2)"""
#     if target_word == "":
#         return 1
#     result = 0

#     for word in word_list:
#         if target_word.startswith(word):
#             remaining = target_word[len(word) :]
#             result = result + count_construct_recur(remaining, word_list)
#     return result


# print(count_construct_recur("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
# print(count_construct_recur("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
# print(
#     count_construct_recur(
#         "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boards"]
#     )  # 0
# )
# print(
#     count_construct_recur("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
# )  # 4
# print(
#     count_construct_recur(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]
#     )
# )  # 0


# def count_construct_recur_memoization(
#     target_word: str, word_list: list, memo: dict
# ) -> bool:
#     """Optimized recursive with memoization, time = O(n^m * m) -> exponential, space = O(m^2)"""
#     if target_word in memo:
#         return memo[target_word]
#     if target_word == "":
#         return 1
#     result = 0

#     for word in word_list:
#         if target_word.startswith(word):
#             remaining = target_word[len(word) :]
#             returned_count = count_construct_recur_memoization(
#                 remaining, word_list, memo
#             )
#             result += returned_count
#     memo[target_word] = result
#     return result


# print(
#     count_construct_recur_memoization("abcdef", ["ab", "abc", "cd", "def", "abcd"], {})
# )  # 1
# print(
#     count_construct_recur_memoization("purple", ["purp", "p", "ur", "le", "purpl"], {})
# )  # 2
# print(
#     count_construct_recur_memoization(
#         "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boards"], {}
#     )  # 0
# )
# print(
#     count_construct_recur_memoization(
#         "enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}
#     )
# )  # 4
# print(
#     count_construct_recur_memoization(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"], {}
#     )
# )  # 0


def count_construct_table(target_word: str, word_list: list) -> bool:
    """Optimized with table, time = O(n^m * m) -> exponential, space = O(m^2)"""
    table = [0 for _ in range(len(target_word) + 1)]
    table[0] = 1
    for i in range(len(target_word)):
        for word in word_list:
            if (i + len(word)) <= len(target_word):
                if target_word[i : (i + len(word))] == word:
                    table[i + len(word)] += table[i]
    return table[len(target_word)]


print(count_construct_table("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
print(count_construct_table("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
print(
    count_construct_table(
        "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boards"]
    )  # 0
)
print(
    count_construct_table("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
)  # 4
print(
    count_construct_table(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]
    )
)  # 0
