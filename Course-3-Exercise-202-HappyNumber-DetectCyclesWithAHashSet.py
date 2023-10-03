class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def get_next(n):
            total_sum = 0
            while n > 0:
                n, digit = divmod(n, 10)
                print(n)
                total_sum += digit ** 2
            print(f"totalsum: {total_sum}")
            return total_sum
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)

        return n == 1






if __name__ == "__main__":

    solution = Solution()

    n1 = 19

    n2 = 2

    outcome1 = solution.isHappy(n1)
    # outcome2 = solution.isHappy(n2)

    print(f"Outcome1: {outcome1}")
