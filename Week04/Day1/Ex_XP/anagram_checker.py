class AnagramChecker:
    def __init__(self):
        with open("sowpods.txt") as file:
            self.words = file.read().splitlines()
    
    def is_valid_word(self,word):
        if word.upper() in self.words:
            return True
        return False
    

    def is_anagram(self, word1, word2):
        word1 = word1.upper()
        word2 = word2.upper()
        if sorted(word1) == sorted(word2) and word1!=word2:
            return True
        return False
    
    def get_anagrams(self, word):
        anagrams = []
        for w in self.words:
            if self.is_anagram(word, w):
                anagrams.append(w.lower())
        return anagrams