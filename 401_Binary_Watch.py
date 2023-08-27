from typing import List


class Solution:
    def readBinaryWatch(turnedOn: int) -> List[str]:
        lst = []
        for hrs in range(12):  # 12hrs
            for mins in range(60):  # 60 min
                if ((bin(hrs) + bin(mins)).count('1') == turnedOn):
                    # 4:03  -> 4--> 100 + 3-> 011 ----> count 1 --> 3
                    time = '%d:%02d' % (hrs, mins)
                    lst.append(time)
        return lst

print(Solution.readBinaryWatch(1))