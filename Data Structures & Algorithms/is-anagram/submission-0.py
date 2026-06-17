class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count1 = [0] * 26
        count2 = [0] * 26
        
        for i in s:
            value = ord(i) - ord('a')
            count1[value] +=1
        
        for j in t:
            value = ord(j) - ord('a')
            count2[value]+=1

        for i in range(26):
            if count1[i] != count2[i]:
                return False
                
        return True
        