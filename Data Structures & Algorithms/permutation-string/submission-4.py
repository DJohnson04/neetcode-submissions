class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        map = {}
        win_map = {}
        for char in s1:
            if char in map:
                map[char] += 1
            else:
                map[char] = 1
        for j in range(len(s1)):
            if s2[j] in win_map:
                win_map[s2[j]] += 1
            else:
                win_map[s2[j]] = 1
            
        if win_map.items() == map.items():
            return True
        for i in range(len(s1), len(s2)):
            removed_character = s2[i - len(s1)]
            win_map[removed_character] -= 1
            if win_map[removed_character] == 0:
                win_map.pop(removed_character)
            ##handle new character
            if s2[i] in win_map.keys():
                 win_map[s2[i]] += 1
            else:
                win_map[s2[i]] = 1
            if win_map.items() == map.items():
                return True
        return False
                
        