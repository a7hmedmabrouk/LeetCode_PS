class Solution(object):
    def maxScoreWords(self, words, letters, score):
        """
        :type words: List[str]
        :type letters: List[str]
        :type score: List[int]
        :rtype: int
        """
        def calculate_word_score(word):
            return sum(score[ord(c) - ord('a')] for c in word)
        
        def can_form_word(word, letter_count):
            word_count = Counter(word)
            for c in word_count:
                if word_count[c] > letter_count[c]:
                    return False
            return True
        
        def backtrack(index, current_score, letter_count):
            if index == len(words):
                return current_score
            
            max_score = current_score
            
            max_score = max(max_score, backtrack(index + 1, current_score, letter_count))
            
            word = words[index]
            if can_form_word(word, letter_count):
                new_letter_count = letter_count.copy()
                for c in word:
                    new_letter_count[c] -= 1
                max_score = max(max_score, backtrack(index + 1, current_score + word_scores[index], new_letter_count))
            
            return max_score
        
        word_scores = [calculate_word_score(word) for word in words]
        
        letter_count = Counter(letters)
        
        return backtrack(0, 0, letter_count)