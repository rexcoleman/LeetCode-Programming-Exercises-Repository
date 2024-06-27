from collections import defaultdict, deque
from typing import List


class Solution:

    def __init__(self):
        self.length = 0
        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        self.all_combo_dict = defaultdict(list)

    def visitWordNode(self, queue, visited, others_visited):
        queue_size = len(queue)
        for _ in range(queue_size):
            current_word = queue.popleft()
            for i in range(self.length):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + '*' + current_word[i+1:]

                # Next states are all the words which share the same intermediate state.
                for word in self.all_combo_dict[intermediate_word]:
                    # If the intermediate state/word has already been visited from the
                    # other parallel traversal this means we have found the answer.
                    if word in others_visited:
                        return visited[current_word] + others_visited[word]
                    if word not in visited:
                        # Save the level as the value of the dictionary, to save number of hops.
                        visited[word] = visited[current_word] + 1
                        queue.append(word)
        return None


    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        self.length = len(beginWord)

        for word in wordList:
            for i in range(self.length):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                self.all_combo_dict[word[:i] + "*" + word[i+1:]].append(word)

        # Queues for birdirectional BFS
        queue_begin = deque([beginWord])  # BFS starting from beginWord
        queue_end = deque([endWord])  # BFS starting from endWord

        # Visited to make sure we don't repeat processing same word
        visited_begin = {beginWord: 1}
        visited_end = {endWord: 1}
        ans = None

        # We do a birdirectional search starting one pointer from begin
        # word and one pointer from end word. Hopping one by one.

        while queue_begin and queue_end:

            # Progress forward one step from the shorter queue
            if len(queue_begin) <= len(queue_end):
                ans = self.visitWordNode(queue_begin, visited_begin, visited_end)
            else:
                ans = self.visitWordNode(queue_end, visited_end, visited_begin)
            if ans:
                return ans

        return 0


if __name__ == '__main__':

    # Inputs and Expected Outputs
    beginWord_1 = "hit"
    endWord_1 = "cog"
    wordList_1 = ["hot", "dot", "dog", "lot", "log", "cog"]
    expected_output_1 = 5
    beginWord_2 = "hit"
    endWord_2 = "cog"
    wordList_2 = ["hot", "dot", "dog", "lot", "log"]
    expected_output_2 = 0

    # Run Tests
    solution_1 = Solution()
    solution_2 = Solution()
    test_1 = solution_1.ladderLength(beginWord_1, endWord_1, wordList_1)
    test_2 = solution_2.ladderLength(beginWord_2, endWord_2, wordList_2)

    # Print Results
    print(f"\nTest 1 Output: {test_1} \nExpected Output: {expected_output_1}")
    print(f"\nTest 2 Output: {test_2} \nExpected Output: {expected_output_2}")