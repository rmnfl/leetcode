class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for s in strs:
            anagrams[str(sorted(s))].append(s)
    
        return anagrams.values()