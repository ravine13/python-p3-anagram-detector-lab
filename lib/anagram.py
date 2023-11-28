class Anagram:
    def __init__(self, word = "word"):
        self.word = word
        self.list = []
    
        
    def match(self,list):
        anagram_list = []
        anagram_letters = [letter for letter in self.word]
        for item in list:
            item_letters = [letter for letter in item]
            if sorted(anagram_letters) == sorted(item_letters):
                anagram_list.append(item)
        return anagram_list