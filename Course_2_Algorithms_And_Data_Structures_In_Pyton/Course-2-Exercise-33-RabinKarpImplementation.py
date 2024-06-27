class RabinKarp:

    def __init__(self, pattern, text):
        self.pattern = pattern
        self.text = text
        # the size of the alphabet (26)
        self.d = 26
        # prime number for the (%) modulo operator
        self.q = 31

    def search(self):
        m = len(self.pattern)
        n = len(self.text)

        # hashes for the region of text and the pattern
        hash_text = 0
        hash_pattern = 0
        # the largest polynomial term in the fingerprint function
        h = 1

        for _ in range(m - 1):
            h = (h * self.d) % self.q

        # pre-compute the pattern in O(M)
        for i in range(m):
            hash_pattern = (self.d * hash_pattern + ord(self.pattern[i])) % self.q
            hash_text = (self.d * hash_text + ord(self.text[i])) % self.q

        # slide the pattern over the text one by one
        for i in range(n - m + 1):

            # check the hash values of the current window of text
            # and pattern. If the hash values match then only
            # check for characters one by one
            if hash_text == hash_pattern:
                # naive approach to check the characters
                j = 0
                while j < m:
                    if self.text[i + j] != self.pattern[j]:
                        break
                    j += 1

                if j == m:
                    print("Found match at index %s" % i)

            # update the hash for the actual substring of the text
            # apply the rolling hash approach
            if i < n - m:
                hash_text = ((hash_text - ord(self.text[i]) * h) * self.d + ord(self.text[i + m])) % self.q

                # we might get a negative value so we have to make sure the hash is positive
                if hash_text < 0:
                    hash_text = hash_text + self.q

if __name__ == '__main__':

    algorithm = RabinKarp('test', 'this is a test')
    algorithm.search()