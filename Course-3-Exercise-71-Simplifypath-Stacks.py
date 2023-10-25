class Solution:
    def simplifyPath(self, path: str) -> str:
        # Initialize a stack
        stack = []
        # Split the input string on "/" as the delimiter
        # and process each portion one by one
        for portion in path.split("/"):
            # If the current component is a "..", then
            # we pop an entry from the stack if it's non-empty
            if portion == "..":
                if stack:
                    stack.pop()
            elif portion == "." or not portion:
                # A no-op for a "." or an empty string
                continue
            else:
                # Finally, a legitimate directory name, so we add it
                # to our stack
                stack.append(portion)

        # Stitch all the directory names together
        final_str = "/" + "/".join(stack)
        return final_str



if __name__ == '__main__':

    # Inputs
    path_1 = "/home/"
    path_2 = "/../"
    path_3 = "/home//foo/"

    # Run tests

    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.simplifyPath(path_1)
    test_2 = solution_2.simplifyPath(path_2)
    test_3 = solution_3.simplifyPath(path_3)

    print(f"Test 1: {test_1}")
    print('Expected Output 1: "/home"')
    print(f"Test 2: {test_2}")
    print('Expected Output 2: "/"')
    print(f"Test 3: {test_3}")
    print('Expected Output 2: "/home/foo"')