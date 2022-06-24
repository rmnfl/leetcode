class Solution(object):
    def topKFrequent(self, nums, k):
        count = Counter(nums)
        
        heap = []
        for key in count:
            heapq.heappush(heap, (-count[key], key))
            
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
            
        return result
    