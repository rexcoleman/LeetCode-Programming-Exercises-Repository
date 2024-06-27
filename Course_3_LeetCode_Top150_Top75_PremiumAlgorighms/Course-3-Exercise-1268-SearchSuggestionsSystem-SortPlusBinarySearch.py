import bisect
from collections import defaultdict
from typing import List


class Solution:

    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        a = products
        result, prefix = [], ''

        for c in searchWord:
            prefix += c
            i = bisect.bisect_left(products, prefix)
            result.append([w for w in products[i:i+3] if w.startswith(prefix)])
        return result


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