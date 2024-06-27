from collections import defaultdict


class WordDictionary:

    def __init__(self):
        self.hash_map = defaultdict(set)

    def addWord(self, word: str) -> None:
        self.hash_map[len(word)].add(word)
        print(self.hash_map)

    def search(self, word: str) -> bool:
        word_length = len(word)
        print(self.hash_map)
        for dict_word in self.hash_map[word_length]:
            i = 0
            while i < word_length and (dict_word[i] == word[i] or word[i] == '.'):
                i += 1
            if i == word_length:
                return True
        return False

if __name__ == '__main__':

    # Inputs and Expected Outputs
    commands = ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    words = [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    expected_output = [None,None,None,None,False,True,True,True]

    # Implement Trie
    word_dictionary = WordDictionary()
    output = [expected_output[0]]
    for i in range(1, len(commands)):
        method = getattr(word_dictionary, commands[i])
        if words[i]:
            result = method(words[i][0])
            output.append(result)
    print(f"\nTest Output: {output} \nExpected Output: {expected_output}")