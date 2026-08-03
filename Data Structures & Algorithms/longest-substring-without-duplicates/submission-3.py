class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        curr_sub = ""
        for char in s:
            if char not in curr_sub:
                curr_sub += char
            else:
                curr_sub = curr_sub[curr_sub.find(char) + 1:] + char
            if len(curr_sub) > length:
                length = len(curr_sub)
        return length
