class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        freq = {}
        left = 0
        ans = 0

        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right], 0) + 1

            while freq[s[right]] > 2:
                freq[s[left]] -= 1
                left += 1
            ans = max(ans, right-left+1)
        return ans
        #Brute force but accepted

        # ans = 0
        # for i in range(len(s)):
        #     freq = {}
        #     for j in range(i, len(s)):
        #         freq[s[j]] = freq.get(s[j], 0) + 1

        #         if freq[s[j]] > 2:
        #             break
        #         ans = max(ans, j-i+1)
        # return ans