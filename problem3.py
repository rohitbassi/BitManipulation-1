class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        ans=int(dividend/divisor)
        if ans > (1 << 31) - 1: return (1 << 31) - 1
        if ans < -(1 << 31): return - (1<<31)
        return ans