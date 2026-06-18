class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = 0
        i,j = 0,len(heights) -1
        while i < j:
            min_height = min(heights[i],heights[j])
            diff = j-i
            capacity = min_height * diff
            res = max(res,capacity)

            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return res
