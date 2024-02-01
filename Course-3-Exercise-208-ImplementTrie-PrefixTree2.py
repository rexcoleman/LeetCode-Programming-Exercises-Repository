class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        trie = self.trie
        for letter in word:
            if letter not in trie:
                trie[letter] = {}
            trie = trie[letter]
        trie['$'] = True

    def search(self, word: str) -> bool:
        trie = self.trie
        for letter in word:
            if letter not in trie:
                return False
            trie = trie[letter]
        return '$' in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for letter in prefix:
            if letter not in trie:
                return False
            trie = trie[letter]
        return True


if __name__ == '__main__':

    commands = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
    values = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    expected_output = [None, None, True, False, True, None, True]
    output = [None,]

    trie = Trie()
    for i in range(1, len(commands)):
        if commands[i] == "insert":
            trie.insert(values[i][0])
            output.append(None)
        elif commands[i] == "search":
            output.append(trie.search(values[i][0]))
        else:
            output.append(trie.startsWith(values[i][0]))

    print(f"\nTest 1 Output: {output} \nExpected Output: {expected_output}")