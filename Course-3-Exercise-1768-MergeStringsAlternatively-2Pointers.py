class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:


        # Create new string for output
        output = ""
        i, j = 0, 0
        switch = 1

        # Use while loop to build output string according to problem statement alternative requirements
        while i < len(word1) and j < len(word2):
            if switch == 1:
                output += word1[i]
                i += 1
                switch = 2
            else:
                output += word2[j]
                j += 1
                switch = 1
        if i == len(word1):
            output += word2[j:]
        else:
            output += word1[j:]
        return output


if __name__ == '__main__':

    # Inputs and Expected Outputs
    word1_1 = "abc"
    word2_1 = "pqr"
    expected_output_1 = "apbqcr"
    word1_2 = "ab"
    word2_2 = "pqrs"
    expected_output_2 = "apbqrs"
    word1_3 = "abcd"
    word2_3 = "pq"
    expected_output_3 = "apbqcd"

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    test_1 = solution_1.mergeAlternately(word1_1, word2_1)
    test_2 = solution_2.mergeAlternately(word1_2, word2_2)
    test_3 = solution_3.mergeAlternately(word1_3, word2_3)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")