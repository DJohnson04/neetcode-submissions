class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        lcp = ''
        if len(strs) == 0:
            return ''
        base_string = strs[0]
        i = 0
        while i < len(base_string):
            for index, string in enumerate(strs):
                if len(string) == i or len(string) < i:
                    return lcp
                if string[i] == base_string[i] and index == len(strs) - 1:
                    lcp += base_string[i]
                    i+=1
                elif string[i] != base_string[i]:
                    return lcp
            
        print("here")
        return lcp