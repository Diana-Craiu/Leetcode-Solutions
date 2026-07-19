from collections import Counter
from typing import Optional

class Solution:
    def reorganizeString(self, s: str) -> str:
        string_length = len(s)
        char_frequency = Counter(s)
        max_frequency = max(char_frequency.values())

        if max_frequency > (string_length + 1) // 2:
            return ''
      
        result = [None] * string_length
      
        current_index = 0
        for character, frequency in char_frequency.most_common():
            while frequency > 0:
                result[current_index] = character
                frequency -= 1
              
                current_index += 2

                if current_index >= string_length:
                    current_index = 1
      
        return ''.join(result)