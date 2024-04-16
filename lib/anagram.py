class Anagram:
    def __init__(self, word):
        self.word = word

    def match(self, word_list):
        matched_word = [letter for letter in self.word]
        anagrams = []
        for word in word_list:
            if (sorted(list(word)) == sorted(matched_word)):
                anagrams.append(word)
        return anagrams