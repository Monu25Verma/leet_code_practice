class Solution:
    def find_div(num):
        result1 = []
        for i in range(1, num + 1):
            if num % i == 0:
                result1.append(i)
        return result1

    def findGCD(self, nums: List[int]) -> int:

        s = sorted(nums)
        small_val = s[0]  # 3
        large_val = s[-1]  # 8
        result_s = find_div(small_val)
        result_l = find_div(large_val)
        if len(result_s) > len(result_l):
            max_list = result_l
            min_list = result_s

        else:
            max_list = result_l
            min_list = result_s
        result = []
        for i in max_list:
            if i in min_list:
                result.append(i)
        return max(sorted(result))
