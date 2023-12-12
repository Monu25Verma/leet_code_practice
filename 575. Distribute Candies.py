class Solution:
    def distributeCandies(candyType: list[int]) -> int:
        updated_candies = set(candyType)
        return min(len(updated_candies), len(candyType) // 2)


print(Solution.distributeCandies([1, 1, 2, 2, 3, 3]))
