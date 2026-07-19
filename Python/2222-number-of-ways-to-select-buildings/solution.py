class Solution:
    def numberOfWays(self, s: str) -> int:
        left_count = [0, 0] 
    
        right_count = [s.count("0"), s.count("1")]
      
        total_ways = 0
      
        for digit in map(int, s):
            right_count[digit] -= 1
            opposite_digit = digit ^ 1
            total_ways += left_count[opposite_digit] * right_count[opposite_digit]
    
            left_count[digit] += 1
      
        return total_ways
            
