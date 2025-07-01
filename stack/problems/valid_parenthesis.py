# https://leetcode.com/problems/valid-parentheses/


def is_balanced_parentheses(s):
    stack_list = []
    ans = {")": "(", "}": "{", "]": "["}
    for val in s:
        if val not in ans:
            stack_list.append(val)
        else:
            if stack_list and stack_list[-1] == ans[val]:
                stack_list.pop()
            else:
                return False
    return len(stack_list) == 0


def test_is_balanced_parentheses():
    try:
        assert is_balanced_parentheses("((()))") == True
        print("Test case 1 passed")
    except AssertionError:
        print("Test case 1 failed")

    try:
        assert is_balanced_parentheses("()") == True
        print("Test case 2 passed")
    except AssertionError:
        print("Test case 2 failed")

    try:
        assert is_balanced_parentheses("(()())") == True
        print("Test case 3 passed")
    except AssertionError:
        print("Test case 3 failed")

    try:
        assert is_balanced_parentheses("(()") == False
        print("Test case 4 passed")
    except AssertionError:
        print("Test case 4 failed")

    try:
        assert is_balanced_parentheses("())") == False
        print("Test case 5 passed")
    except AssertionError:
        print("Test case 5 failed")

    try:
        assert is_balanced_parentheses(")(") == False
        print("Test case 6 passed")
    except AssertionError:
        print("Test case 6 failed")

    try:
        assert is_balanced_parentheses("") == True
        print("Test case 7 passed")
    except AssertionError:
        print("Test case 7 failed")

    try:
        assert is_balanced_parentheses("()()()()") == True
        print("Test case 8 passed")
    except AssertionError:
        print("Test case 8 failed")

    try:
        assert is_balanced_parentheses("(())(())") == True
        print("Test case 9 passed")
    except AssertionError:
        print("Test case 9 failed")

    try:
        assert is_balanced_parentheses("(()()())") == True
        print("Test case 10 passed")
    except AssertionError:
        print("Test case 10 failed")

    try:
        assert is_balanced_parentheses("((())") == False
        print("Test case 11 passed")
    except AssertionError:
        print("Test case 11 failed")


test_is_balanced_parentheses()
