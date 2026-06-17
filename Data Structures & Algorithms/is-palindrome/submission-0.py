class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned_str = re.sub(r'[^A-Za-z0-9]', '', s).lower()
        rev = cleaned_str[::-1]
        return cleaned_str == rev