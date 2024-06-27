# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0

def guess(num: int) -> int:
    if num == pick:
        return 0
    elif num < pick:
        return 1
    else:
        return -1


class Solution:
    def guessNumber(self, n: int) -> int:
        a = 5 // 2
        b = 5 >> 1

        lower_bound, upper_bound = 1, n
        # Binary division faster than (lowerBound + upperBound) // 2
        myGuess = (lower_bound + upper_bound) >> 1
        # walrus operator ':=' - assigns value of the function to the variable 'res'
        # and then compare res with 0
        while (res := guess(myGuess)) != 0:
            if res == 1:
                lower_bound = myGuess + 1
            else:
                upper_bound = myGuess - 1
            myGuess = (lower_bound + upper_bound) >> 1

        return myGuess




if __name__ == '__main__':
    solution = Solution()

    # Define picks for each test
    picks = {1: 6, 2: 1, 3: 1}

    # Run Tests
    for test_id, pick_value in picks.items():
        global pick
        pick = pick_value
        if test_id == 1:
            assert solution.guessNumber(10) == pick
        elif test_id == 2:
            assert solution.guessNumber(1) == pick
        elif test_id == 3:
            assert solution.guessNumber(2) == pick

    print("All tests passed!")
