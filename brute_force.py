
# linear search

def linear(items, find):
    for sets, val in enumerate(items):
        if val == find:
            return sets
    return -1


print(linear([1, 24, 7, 3, 7, 9, 8], 9))
def max_val(nums):
    for i in range(len(nums)):
        for j in range(i):

            def maxSubArray(nums):
                n = len(nums)
                prefix = [0] * (n + 1)
                for i in range(1, n + 1):
                    prefix[i] = prefix[i - 1] + nums[i - 1]
                maxSum = float('-inf')
                for i in range(n):
                    for j in range(i, n):
                        sum = prefix[j + 1] - prefix[i]
                        maxSum = max(maxSum, sum)
                return maxSum

