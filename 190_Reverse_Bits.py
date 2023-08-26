class Solution:
    def reverseBits(n: int) -> int:
        # signed - zero and positive
        # unsigned - positive and negative, zero
        output = 0
        for _ in range(0, 32):
            output <<= 1
            if n & 1:
                output += 1
            n >>= 1
        return output

print(Solution.reverseBits(0o0000010100101000001111010011100))






