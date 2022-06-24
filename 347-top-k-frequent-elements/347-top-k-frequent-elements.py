class Solution(object):
    def topKFrequent(self, nums, k):
        return list(zip(*Counter(nums).most_common(k)))[0]
    