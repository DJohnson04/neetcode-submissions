class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        map = {}
        for char in s1:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1
        window = len(s1)
        for index in range(len(s2) - window + 1):
            win_map = {}
            for char in range(index, index + window):
                if s2[char] in win_map:
                    win_map[s2[char]] += 1
                else:
                    win_map[s2[char]] = 1
            print(win_map.items())
            if win_map.items() == map.items():
                return True
        return False
                
        