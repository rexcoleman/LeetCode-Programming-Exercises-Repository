import bisect
from collections import defaultdict


class Solution:
    def shortestWay(self, source: str, target: str) -> int:

        # Length of source
        source_length = len(source)

        # Next Occurrence of Character after Index
        next_occurrence = [defaultdict(int) for idx in range(source_length)]

        # Base Case
        next_occurrence[source_length -
                        1][source[source_length - 1]] = source_length - 1

        # Using Recurrence Relation to fill next_occurrence
        for idx in range(source_length - 2, -1, -1):
            next_occurrence[idx] = next_occurrence[idx + 1].copy()
            next_occurrence[idx][source[idx]] = idx

        # Pointer for source
        source_iterator = 0

        # Number of times we need to iterate through source
        count = 1

        # Find all characters of target in source
        for char in target:

            # If character is not in source, return -1
            if char not in next_occurrence[0]:
                return -1

            # If we have reached the end of source, or the character is not in
            # source after source_iterator, loop back to beginning
            if (source_iterator == source_length or
                    char not in next_occurrence[source_iterator]):
                count += 1
                source_iterator = 0

            # Next occurrence of character in source after source_iterator
            source_iterator = next_occurrence[source_iterator][char] + 1

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