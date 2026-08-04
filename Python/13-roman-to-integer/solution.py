class Solution:
    def romanToInt(self, s: str) -> int:
        
        numere = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M" : 1000
            }

        numar=0

        for i in range(len(s) - 1):
            if numere[s[i]] < numere[s[i + 1]]:
                numar -= numere[s[i]]
            else:
                numar += numere[s[i]]
            
        numar+=numere[s[-1]]

        return numar

        
