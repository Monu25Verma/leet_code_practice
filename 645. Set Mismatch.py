from collections import Counter
nums = [1,2,2,4]
# count = 0
# dup_present = []
# for i in range(len(nums)):
#     k = i +1
#     for j in range(k, len(nums)):
#         if nums[i] == nums[j] and nums[i] not in dup_present:
#             dup_present.append(nums[i])
#
# nums.sort()
# duplicate = list(set(nums))
# dup = sum(duplicate)
# print(dup)
# miss_val = len(nums)*(len(nums)+1)//2
# print(miss_val)
# val =  miss_val - dup
# dup_present.append(val)
# print(dup_present)
#


# c = Counter(nums)
# l  = [0, 0]
# for i in range(1, len(nums)+1):
#     if c[i] == 2:
#         l[0] = i
#     if c[i] == 0:
#         l[1] = i
# print(l[0], l[1])

nums.sort()
dic = {}
result = []
for i in range(1, len(nums)+1):
    dic[i] = 0
for i in nums:
    if i in dic:
        dic[i] += 1
for i, j in dic.items():
    if j == 0 or j == 2:
        result.append(i)
print(result)



