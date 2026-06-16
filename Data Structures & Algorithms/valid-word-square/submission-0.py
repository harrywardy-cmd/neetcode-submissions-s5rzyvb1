class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for word in range(len(words)):
            for char_pos in range(len(words[word])):
                if char_pos >=len(words) or word >= len(words[char_pos]) or words[word][char_pos] != words[char_pos][word]:
                    return False
        return True
        