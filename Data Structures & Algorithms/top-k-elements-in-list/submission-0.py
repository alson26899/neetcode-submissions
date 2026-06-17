class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = defaultdict(int)
        res = []
        occurence = 0
        for num in nums:
            groups[num] +=1
        
        sorted_dict = dict(sorted(groups.items(), key = lambda item: item[1], reverse = True))

        for count in sorted_dict:
            if occurence >= k:
                break
            res.append(count)
            occurence += 1

        return res