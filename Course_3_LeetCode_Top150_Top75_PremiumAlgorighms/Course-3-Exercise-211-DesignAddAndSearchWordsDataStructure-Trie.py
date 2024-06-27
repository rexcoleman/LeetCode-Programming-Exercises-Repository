from collections import defaultdict


class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        node = self.trie
        for letter in word:
            if letter not in node:
                node[letter] = {}
            node = node[letter]
        node['$'] = True

    def search(self, word: str) -> bool:

        def search_in_node(word, node) -> bool:
            for i, letter in enumerate(word):
                if letter not in node:
                    # if the current character is '.' check all possible nodes at this level
                    if letter == '.':
                        for x in node:
                            if x != '.' and search_in_node(word[i + 1:], node[x]):
                                return True

                    # If no nodes lead to answer or the current character != '.'
                    return False
                # If the character is found go down to the next level in trie
                else:
                    node = node[letter]
            return '$' in node
        return search_in_node(word, self.trie)


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