class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = {}
        left = 0
        max_len = 0

        for i in range(len(s)):
            chars[s[i]] = chars.get(s[i],0) + 1

            window_len = i - left + 1
            max_count = max(chars.values())

            if window_len - max_count > k:
                chars[s[left]] -= 1
                left += 1
            
            max_len = max(max_len, i - left + 1)

        return max_len
        