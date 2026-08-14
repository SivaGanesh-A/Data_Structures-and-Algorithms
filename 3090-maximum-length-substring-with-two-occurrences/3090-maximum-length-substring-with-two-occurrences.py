class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        ans = 0
        for i in range(len(s)):
            freq = {}
            for j in range(i, len(s)):
                freq[s[j]] = freq.get(s[j], 0) + 1

                if freq[s[j]] > 2:
                    break
                ans = max(ans, j-i+1)
        return ans