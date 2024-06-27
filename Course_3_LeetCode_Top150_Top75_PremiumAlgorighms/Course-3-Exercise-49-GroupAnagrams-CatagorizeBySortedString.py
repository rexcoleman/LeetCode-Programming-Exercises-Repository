from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()



if __name__ == '__main__':

    # Inputs
    strs_1 = ["eat", "tea", "tan", "ate", "nat", "bat"]
    strs_2 = [""]
    strs_3 = ["a"]

    # Run tests
    solution_1 = Solution()
    solution_2 = Solution()
    solution_3 = Solution()

    test_1 = solution_1.groupAnagrams(strs_1)
    test_2 = solution_2.groupAnagrams(strs_2)
    test_3 = solution_3.groupAnagrams(strs_3)

    print(f"Test 1: {test_1}")
    print('Expected Output 1: [["bat"],["nat","tan"],["ate","eat","tea"]]')
    print(f"Test 2: {test_2}")
    print('Expected Output 2: [[""]]')
    print(f"Test 2: {test_3}")
    print('Expected Output 3: [["a"]]')
