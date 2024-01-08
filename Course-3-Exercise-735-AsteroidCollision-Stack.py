from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for a in asteroids:
            while s and s[-1] > 0 and a < 0:
                if s[-1] + a < 0:
                    s.pop()
                elif s[-1] + a > 0:
                    break
                else:
                    s.pop()
                    break
            else:
                s.append(a)
        return s


if __name__ == '__main__':
    # Inputs and Expected Outputs:
    asteroids_1 = [5, 10, -5]
    expected_output_1 = [5, 10]
    asteroids_2 = [8, -8]
    expected_output_2 = []
    asteroids_3 = [10, 2, -5]
    expected_output_3 = [10]
    asteroids_4 = [-2, -1, 1, 2]
    expected_output_4 = [-2, -1, 1, 2]

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()
    solution_4 = Solution()
    test_1 = solution_1.asteroidCollision(asteroids_1)
    test_2 = solution_2.asteroidCollision(asteroids_2)
    test_3 = solution_3.asteroidCollision(asteroids_3)
    test_4 = solution_4.asteroidCollision(asteroids_4)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")
    print(f"\nTest 3 Output: {test_3} \nExpected Output: {expected_output_3}")
    print(f"\nTest 4 Output: {test_4} \nExpected Output: {expected_output_4}")
