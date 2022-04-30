class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()
        res = ""
        sign = None

        if not s:
            return 0
        
        if s[0] in "+-":
            sign = (0 if s[0]=="-" else 1)
            s = s[1:]
        else:
            sign = 1
        
        for char in s:
            if char.isdigit():
                res += char
            else:
                break
        
        res = (int(res) if len(res) > 0 else 0)        
        res =  (res if sign else -res) 
        
        if res < -2**31:
            return -2**31
        elif res > 2**31 - 1:
            return 2**31 - 1
        else: 
            return res
        