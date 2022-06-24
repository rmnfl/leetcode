class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord("a")] += 1
            anagrams[tuple(counter)].append(s)
    
        return anagrams.values()