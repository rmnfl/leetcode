class Solution:
    def intToRoman(self, num: int) -> str:
        romans = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        numbers = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        
        result = ""
        
        for n, r in zip(numbers, romans):
            result += r * (num // n)
            num %= n
            
        return result
