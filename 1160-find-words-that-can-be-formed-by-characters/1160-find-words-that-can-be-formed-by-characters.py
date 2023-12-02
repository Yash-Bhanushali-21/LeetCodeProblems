from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        c_count = {}
        count = 0
        
        # Count the occurrences of each character in chars
        for x in chars:
            if x in c_count:
                c_count[x] += 1
            else:
                c_count[x] = 1
        
        # Check if the word can be formed from chars
        for word in words:
            isTrue = True
            word_count = {}  # Count of occurrences of each character in the word
            
            # Count the occurrences of each character in the word
            for c in word:
                if c in word_count:
                    word_count[c] += 1
                else:
                    word_count[c] = 1
            
            # Check if the word can be formed from chars
            for c, freq in word_count.items():
                if c in c_count and c_count[c] >= freq:
                    continue
                else:
                    isTrue = False
                    break
            
            # If the word can be formed, add its length to the count
            if isTrue:
                count += len(word)
        
        return count
