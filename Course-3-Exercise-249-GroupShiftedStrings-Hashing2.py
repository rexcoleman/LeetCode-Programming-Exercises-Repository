from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:

        # Create a hash value
        def get_hash(string: str):
            key = []
            for a, b in zip(string, string[1:]):
                key.append(chr((ord(b) - ord(a)) % 26 + ord('a')))
            return ''.join(key)

        # Create a hash value (hash_key) for each string and append the string
        # to the list of hash values i.e. mapHashToList["cd"] = ["acf", "gil", "xzc"]
        groups = defaultdict(list)
        for string in strings:
            hash_key = get_hash(string)
            groups[hash_key].append(string)

        # Return a list of all of the grouped strings
        return list(groups.values())


if __name__ == '__main__':

    # Inputs and Expected Outputs
    strings_1 = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    expected_output_1 = [["acef"], ["a", "z"], ["abc", "bcd", "xyz"], ["az", "ba"]]
    strings_2 = ["a"]
    expected_output_2 = [["a"]]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.groupStrings(strings_1)
    test_2 = solution_2.groupStrings(strings_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")