class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        if n <= 0:
            return 0
        res = 0
        pre = [0] * n
        suf = [0] * n

        pre[0] = height[0]
        suf [n-1] = height[n-1]
        for i in range(1,n):
            pre[i] = max(pre[i-1],height[i])

        for i in range(n-2,-1,-1):
            suf[i] = max(suf[i+1],height[i])
        
        for i in range(n):
            trap = min(pre[i],suf[i]) - height[i]

            if trap > 0:
                res +=trap
        
        return res