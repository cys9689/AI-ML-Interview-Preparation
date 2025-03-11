class Solution:
    def _isVowel(self,c:str)->bool:
        return c in ["a", "e", "i", "o", "u"]

    def countOfSubstrings(self, word: str, k: int) -> int:
        result = 0
        start = end = 0
        vowel_count = {}
        consonant_count = 0
        next_consonant = [0] * len(word)
        next_consonant_index = len(word)
        for i in range(len(word) -1 , -1 , -1):
            next_consonant[i] = next_consonant_index
            if not self._isVowel(word[i]):
                next_consonant_index = i
        while end < len(word):
            new_letter = word[end]
            if self._isVowel(new_letter):
                vowel_count[new_letter] = vowel_count.get(new_letter,0)+1
            else:
                consonant_count +=1
            while (consonant_count > k):
                start_letter = word[start]
                if self._isVowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -= 1
                start +=1
            while ( 
                start <len(word)
                and len(vowel_count) == 5
                and consonant_count ==k):
                result += next_consonant[end] - end
                start_letter = word[start]
                if self._isVowel(start_letter):
                    vowel_count[start_letter] -= 1
                    if vowel_count[start_letter] == 0:
                        del vowel_count[start_letter]
                else:
                    consonant_count -=1
                start +=1


            end +=1
        return result



solution = Solution()
print("Test Case 1:" , solution.countOfSubstrings("aeioqq",1))
print("Test Case 2:" , solution.countOfSubstrings("aeiou",0))
print("Test Case 3:" , solution.countOfSubstrings("ieaouqqieaouqq",1))

