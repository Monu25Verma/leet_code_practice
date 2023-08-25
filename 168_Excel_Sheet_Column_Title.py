class Solution:
    def convertToTitle(columnNumber: int) -> str:
        res=""
        while(columnNumber>0):
            columnNumber-=1
            i=columnNumber%26
            res+=chr(65+i)
            columnNumber=columnNumber//26
        return res[::-1]

print(Solution.convertToTitle(1))