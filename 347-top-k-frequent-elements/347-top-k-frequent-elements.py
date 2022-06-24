class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        freq = [[] for _ in range(len(nums) + 1)]
        
        for key, value in count.items():
            freq[value].append(key)
        
        result = []
        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:    
                result.append(n)
                if len(result) == k:
                    return result
