class Trie:

    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        current_node = self.trie
        for letter in word:
            if letter not in current_node:
                current_node[letter] = {}
            current_node = current_node[letter]
        current_node["-"] = True

    def search(self, word: str) -> bool:
        current_node = self.trie
        for letter in word:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return "-" in current_node


    def starts_with(self, prefix: str) -> bool:
        current_node = self.trie
        for letter in prefix:
            if letter not in current_node:
                return False
            current_node = current_node[letter]
        return True


if __name__ == '__main__':

    # Inputs and Expected Outputs
    commands = ["Trie", "insert", "search", "search", "starts_with", "insert", "search"]
    word = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
    expected_output = [None, None, True, False, True, None, True]

    # Implement Trie
    trie = Trie()
    output = [None]
    for i in range(1, len(commands)):
        method = getattr(trie, commands[i])
        if word[i]:
            result = method(word[i][0])
            output.append(result)
    print(f"\nTest Output: {output} \nExpected Output: {expected_output}")



