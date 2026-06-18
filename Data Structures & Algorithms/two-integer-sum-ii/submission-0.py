class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        hash_map = defaultdict(int)
        
        for i in range(len(numbers)):
            required = target - numbers[i]

            if required in hash_map:
                return [hash_map[required] + 1, i+1]
            
            hash_map[numbers[i]] = i

        return []
