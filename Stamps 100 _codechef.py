def compare_lexo(s, lex):
    if len(s) >= len(lex):
        if s[0] == '0':
            s = s[1:]
            result = compare_lexo(s, lex)
            return result
        else:
            s_bin = decimal_integer = int(s, 2)
            lex_bin = decimal_integer = int(lex, 2)
            if (s_bin > lex_bin):
                result = lex




            else:
                result = s

            return result


T = int(input())
for testcase in range(T):
    n = int(input())
    s = input()
    lex = '100'
    s_bin = decimal_integer = int(s, 2)
    lex_bin = decimal_integer = int(lex, 2)
    if (s_bin > lex_bin):
        result = lex
    else:
        result = s
    print(result)