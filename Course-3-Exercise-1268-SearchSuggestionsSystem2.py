from collections import defaultdict
from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.products = list()
        self.n = 0


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.node = self.root

    def add_product(self, product):
        node = self.root
        for c in product:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]
            if node.n < 3:
                node.products.append(product)
                node.n += 1

    def find_word_by_prefix(self, c):
        if self.node and c in self.node.children:
            self.node = self.node.children[c]
            return self.node.products
        else:
            self.node = None
            return []


class Solution:

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        trie = Trie()
        for product in products:
            trie.add_product(product)
        return [trie.find_word_by_prefix(c) for c in searchWord]


if __name__ == '__main__':

    # Inputs and Expected Outputs
    products_1 = ["mobile", "mouse", "moneypot", "monitor", "mousepad"]
    searchWord_1 = "mouse"
    expected_output_1 = [["mobile", "moneypot", "monitor"],
                         ["mobile", "moneypot", "monitor"],
                         ["mouse", "mousepad"],
                         ["mouse", "mousepad"],
                         ["mouse", "mousepad"]]
    products_2 = ["havana"]
    searchWord_2 = "havana"
    expected_output_2 = [["havana"], ["havana"], ["havana"], ["havana"], ["havana"], ["havana"]]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.suggestedProducts(products_1, searchWord_1)
    test_2 = solution_2.suggestedProducts(products_2, searchWord_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")