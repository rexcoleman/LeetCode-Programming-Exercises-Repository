class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(number):
            total_sum = 0
            while number > 0:
                number, digit = divmod(number, 10)
                print(number)
                total_sum += digit ** 2
            print(f"totalsum: {total_sum}")
            return total_sum
        slow_runner = n
        fast_runner = get_next(n)
        while fast_runner != 1 and slow_runner != fast_runner:
            slow_runner = get_next(slow_runner)
            fast_runner = get_next(get_next(fast_runner))
        return fast_runner == 1







if __name__ == "__main__":

    solution = Solution()

    n1 = 19

    n2 = 2

    outcome1 = solution.isHappy(n1)
    outcome2 = solution.isHappy(n2)

    print(f"Outcome1: {outcome1}")
    print(f"Outcome2: {outcome2}")
