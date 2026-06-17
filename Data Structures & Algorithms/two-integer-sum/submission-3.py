class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        res = []

        for i in range(0,len(nums)):
            if (target - nums[i]) in hash_map:
                res = [hash_map.get(target - nums[i]),i]
                return res
            hash_map[nums[i]] = i
        return res
