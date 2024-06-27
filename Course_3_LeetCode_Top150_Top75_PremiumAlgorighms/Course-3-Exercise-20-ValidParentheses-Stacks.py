class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # The stack to keep track of opening brackets
        stack = []

        # Hash map for keeping track of mappings. This keeps the code very clean
        # Also makes adding more types of parenthesis easier
        mapping = {
            ")": "(",
            "}": "{",
            "]": "["
        }

        # For every bracket in the expression
        for char in s:
            # If the char is a closing bracket
            if char in mapping:
                # Pop the top most element from the stack if it is not empty.
                # Otherwise assign a dummy value of '#' to the top_element variable
                top_element = stack.pop() if stack else '#'

                # The mapping for the opening bracket is in our hash and the top
                # element of the stack don't match: Return False.
                if mapping[char] != top_element:
                    return False
            else:
                # We have an opening bracket. Simply push it onto the stack.
                stack.append(char)

        # In the end, if the stack is empty, we have a valid expression.
        # The stack wont be empty for cases like: ((()
        return not stack


if __name__ == "__main__":

    solution = Solution()

    s1 = "()"
    s2 = "()[]{}"
    s3 = "(]"

    outcome1 = solution.isValid(s1)
    outcome2 = solution.isValid(s2)
    outcome3 = solution.isValid(s3)

    print(f"Outcome1: {outcome1}")
    print(f"Outcome2: {outcome2}")
    print(f"Outcome3: {outcome3}")