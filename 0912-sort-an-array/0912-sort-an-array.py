class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def mergeSort(arr, s, e):
            if e - s == 0:
                return arr
            
            m = (s + e) // 2
            
            mergeSort(arr, s, m)
            mergeSort(arr, m + 1, e)

            merge(arr, s, m, e)

            return arr
        
        def merge(arr, s, m, e):
            L = arr[s:m+1]
            R = arr[m+1:e+1]

            i = 0
            j = 0
            k = s

            while i < len(L) and j < len(R):
                if L[i] <= R[j]:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1

            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1

        return mergeSort(nums, 0, len(nums))