class Solution(object):
    def isAnagram(self, s, t):
        dict_s = Counter(s)
        dict_t = Counter(t)
        
        return dict_s == dict_t