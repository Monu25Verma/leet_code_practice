import math
from typing import List


class Solution:
    def constructRectangle(area: int) -> List[int]:
        x = int(math.sqrt(area))  # x = 349
        while True:
            y = area / x  # 122122 / 349
            if y.is_integer():  # 349
                if x > y:  #
                    return [x, int(y)]
                else:
                    return [int(y), x]

            x -= 1

print(Solution.constructRectangle(122122))