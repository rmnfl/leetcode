class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list)
        
        for s in strs:
            anagrams["".join(sorted(s))].append(s)
    
        return anagrams.values()
    