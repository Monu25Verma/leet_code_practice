import  sys
class Solution:
    def addStrings(num1: str, num2: str) -> str:
        sys.set_int_max_str_digits(10000)
        convert_num1 = int(num1)
        convert_num2 = int(num2)
        convert = convert_num1 + convert_num2
        return str(convert)


print(Solution.addStrings("11", "123"))