input_val = ["))((", "a(bcd(d)", ")abc(d)e", ")))a(bc)d)("]


def check_valid_parenthesis(s):
    index_to_del_stack = []
    s = list(s)
    for index in range(len(s)):
        if s[index] == "(":
            index_to_del_stack.append(index)
        elif s[index] == ")" and len(index_to_del_stack):
            index_to_del_stack.pop()
        elif s[index] == ")":
            s[index] = ""

    for i in index_to_del_stack:
        s[i] = ""

    return "".join(s)


for val in input_val:
    print(check_valid_parenthesis(val))
