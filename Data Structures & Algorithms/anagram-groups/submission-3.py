class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = {}
        count = 0
        result = []
        for word in strs:
            array = [0] * 27
            for char in word:
                value = ord(char.lower()) - 96;
                array[value] += 1
            t = tuple(array)
            if t not in words.keys():
                words[t] = [count]
            else:
                words[t].append(count)
            count += 1 
        sub_list = []

        for indexes in words.values():
            if type(indexes) == int:
                result.append([strs[indexes]])
            else: 
                for index in indexes:
                    sub_list.append(strs[index])
                result.append(sub_list)
                sub_list = []
        return result