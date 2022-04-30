class Solution:
    def romanToInt(self, s: str) -> int:       
        digits = {
            "I": 1,
            "V": 5,
            "X": 10, 
            "L": 50, 
            "C": 100, 
            "D": 500, 
            "M": 1000
        }
        
        result = 0
        previous = None
        
        for char in s[::-1]:
            if previous and digits[char] < digits[previous]:
                result -= digits[char]
            else:
                result += digits[char]
            
            previous = char
            
        return result
    