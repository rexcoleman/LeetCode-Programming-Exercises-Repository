from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        # Move along the input array starting from the end
        for i in range(n):
            idx = n - 1 - i
            # Set all the 9's at the end of the array to zero
            if digits[idx] == 9:
                digits[idx] = 0
            # Here we have the rightmost non 9
            else:
                # Increase this rightmost non 9 by 1
                digits[idx] += 1
                # And the job is done
                return digits
        # We're here because all the digits are 9
        return [1] + digits



if __name__ == '__main__':

    # Inputs
    digits1 = [1,2,3]
    digits2 = [4,3,2,1]
    digits3 = [9]

    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.plusOne(digits1)
    test_2 = solution_2.plusOne(digits2)
    test_3 = solution_3.plusOne(digits3)

    print(f"Test 1: {test_1}")
    print(f"Test 2: {test_2}")
    print(f"Test 3: {test_3}")