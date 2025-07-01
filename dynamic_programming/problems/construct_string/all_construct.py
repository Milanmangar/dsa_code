# https://www.youtube.com/watch?v=oBt53YbR9Kk


# def all_coustruct_recur(target_word: str, word_list: list) -> list:
#     """normal brute force recursive, time = O(n^m * m) -> exponential, space = O(m^2)"""
#     if target_word == "":
#         return [[]]
#     result = []

#     for word in word_list:
#         if target_word.startswith(word):
#             remaining = target_word[len(word) :]
#             suffix_ways = all_coustruct_recur(remaining, word_list)
#             target_ways = []
#             for suffixes in suffix_ways:
#                 target_ways.append([word] + suffixes)
#             result.extend(target_ways)

#     return result


# print(all_coustruct_recur("abcdef", ["ab", "abc", "cd", "def", "abcd"]))  # 1
# print(all_coustruct_recur("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
# print(
#     all_coustruct_recur(
#         "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boards"]
#     )  # 0
# )
# print(
#     all_coustruct_recur("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
# )  # 4
# print(
#     all_coustruct_recur(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]
#     )
# )  # 0


# def all_coustruct_recur_memo(target_word: str, word_list: list, memo: dict) -> list:
#     """Optimized recursive with memoization, time = O(n^m) -> exponential, space = O(m)"""
#     if target_word in memo:
#         return memo[target_word]
#     if target_word == "":
#         return [[]]
#     result = []

#     for word in word_list:
#         if target_word.startswith(word):
#             remaining = target_word[len(word) :]
#             suffix_ways = all_coustruct_recur_memo(remaining, word_list, memo)
#             target_ways = []
#             for suffixes in suffix_ways:
#                 target_ways.append([word] + suffixes)
#             result.extend(target_ways)
#     memo[target_word] = result

#     return result


# print(
#     all_coustruct_recur_memo(
#         "abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"], {}
#     )
# )  # 1
# print(all_coustruct_recur_memo("purple", ["purp", "p", "ur", "le", "purpl"], {}))  # 2
# print(
#     all_coustruct_recur_memo(
#         "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boards"], {}
#     )  # 0
# )
# print(
#     all_coustruct_recur_memo(
#         "enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"], {}
#     )
# )  # 4
# print(
#     all_coustruct_recur_memo(
#         "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"], {}
#     )
# )  # 0


def all_coustruct_table(target_word: str, word_list: list) -> list:
    """Optimized with table, time = O(n^m) -> exponential, space = O(n^m)"""

    table = [[] for _ in range(len(target_word) + 1)]
    table[0] = [[]]
    for i in range(len(target_word)):
        if table[i]:  # no need to proceed if no construction up to here
            for word in word_list:
                if (i + len(word)) <= len(table):
                    if target_word[i : i + len(word)] == word:
                        val = [arr + [word] for arr in table[i]]
                        # print(val)
                        table[i + len(word)].extend(val)

    return table[len(target_word)]


print(all_coustruct_table("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]))  # 1
print(all_coustruct_table("purple", ["purp", "p", "ur", "le", "purpl"]))  # 2
print(
    all_coustruct_table(
        "skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boards"]
    )  # 0
)
print(
    all_coustruct_table("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
)  # 4
print(
    all_coustruct_table(
        "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee"]
    )
)  # 0
