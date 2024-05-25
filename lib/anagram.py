# your code goes here!

class Anagram:
    def __init__(self, word):
        self.word = word.lower()

    def match(self, candidates):
        return [candidate for candidate in candidates if sorted(candidate.lower()) == sorted(self.word)]
