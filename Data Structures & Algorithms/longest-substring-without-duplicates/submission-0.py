class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        chars = {}
        left = 0
        max_len = 0

        for i in range(len(s)):
            # ここに、重複チェック + left更新を入れる
            if s[i] in chars and chars[s[i]] >= left:
                left = chars[s[i]] + 1
        # charsを更新する
            chars[s[i]] = i
        # ウィンドウの長さを計算し、max_lenと比較する
            max_len = max(i - left + 1, max_len)
    
        return max_len