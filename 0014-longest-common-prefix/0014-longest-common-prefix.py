class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = list()

        for chars in zip(*strs):
            if len(set(chars)) == 1:
                result.extend(set(chars))
            else:
                break

        return ''.join(result)
        