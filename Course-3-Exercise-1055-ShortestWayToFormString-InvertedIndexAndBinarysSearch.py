import bisect
from collections import defaultdict


class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        # List of indices for all characters in source
        char_to_indices = defaultdict(list)
        for i, c in enumerate(source):
            char_to_indices[c].append(i)

        # Pointer for source
        source_iterator = 0

        # Number of times we need to iterate through source
        count = 1

        # Find all characters of target in source
        for char in target:
            # If character is not in source, return -1
            if char not in char_to_indices:
                return -1

            # Binary Search to find the index of the character in source
            # next to the current source_iterator
            index = bisect.bisect_left(char_to_indices[char], source_iterator)

            # If we have reached the end of the list, we need to iterate
            # through source again, hence first index of character in source.
            if index == len(char_to_indices[char]):
                count += 1
                source_iterator = char_to_indices[char][0] + 1
            else:
                source_iterator = char_to_indices[char][index] + 1

        # Return the number of times we need to iterate through source
        return count

if __name__ == '__main__':

    # Inputs and Expected Outputs
    source_1 = "abc"
    target_1 = "abcbc"
    expected_output_1 = 2
    source_2 = "abc"
    target_2 = "abcbc"
    expected_output_2 = 2
    source_3 = "xyz"
    target_3 = "xzyxz"
    expected_output_3 = 3

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.shortestWay(source_1, target_1)
    test_2 = solution_2.shortestWay(source_2, target_2)
    test_3 = solution_3.shortestWay(source_3, target_3)

    # Print Test Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")