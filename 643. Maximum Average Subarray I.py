nums = [1,12,-5,-6,50,3]
k = 4

sum_val = 0
for i in range(k):      #0, 1,2,3
    sum_val += nums[i]      #  1 + 12 -> 13
maxI = sum_val          #maxI = 13
for  i in range(k, len(nums)):  #(4,5)
    sum_val += nums[i] - nums[i-k]      # 13 + 50 -
    maxI= max(maxI, sum_val)
print(maxI/k)