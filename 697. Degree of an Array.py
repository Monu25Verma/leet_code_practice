nums = [1,2,2,3,1,4,2]
degree = 0
dic = {}
left = {}
right = {}
count_len = len(nums)
for i, num in enumerate(nums):
    if num in dic:
        dic[num] += 1
    else:
        dic[num] = 1
    degree = max(degree, dic[num])

    if num not in left:
        left[num] = i
    right[num] = i

for num, freq in dic.items():
    if freq == degree:
        count_len = min(count_len, right[num] - left[num] + 1)


print(count_len)










