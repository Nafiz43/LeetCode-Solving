from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs):
        result = defaultdict(list)
        for s in strs:
            count_ch = [0] * 26
            for c in s:
                c_index = ord(c) - ord('a')
                count_ch[c_index] += 1
            result[tuple(count_ch)].append(s)
        return list(result.values())