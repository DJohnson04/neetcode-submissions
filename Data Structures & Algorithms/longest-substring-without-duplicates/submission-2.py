class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        existing = {}
        curr_sub = ""
        for char in s:
            if char not in curr_sub:
                curr_sub += char
                existing[curr_sub] = 1
            else:
                curr_sub = curr_sub[curr_sub.find(char) + 1:] + char
            if curr_sub in existing:
                if len(curr_sub) > length:
                    length = len(curr_sub)
        print(existing.keys())
        return length
