class Solution:
    def romanToInt(self, s: str) -> int:
        I = 1
        V = 5
        X = 10
        L = 50
        C = 100
        D = 500
        M = 1000
        
        roman_nums = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}

        res = 0
        for i in range(len(s)):
            #if i has a character after it then check what the value of that character is
            if i + 1 < len(s) and roman_nums[s[i]] < roman_nums[s[i+1]]:
                #suvtract the value if the value of next character is smaller than 
                res -= roman_nums[s[i]]
            else:
                #other wise add the value
                res += roman_nums[s[i]]
        return res
                
