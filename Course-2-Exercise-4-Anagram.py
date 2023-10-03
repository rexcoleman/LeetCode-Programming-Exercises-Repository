def is_anagram(str1, str2):
    # if the length of the strings differ then they are not anagrams
    if len(str1) != len(str2):
        return False
    # this is the bottleneck because it in 0(NlogN)
    str1 = sorted(str1)
    str2 = sorted(str2)
    print(str1)
    print(str2)
    #check the letters with the same indexes
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    return True


    # Time complexity: O(NlogN)
    # Sorting costs O(NlogN) where N represents the length of str1
    # Comparing strings in for loop costs O(N)
    # O(NlogN) + O(N) = O(NlogN)
    # Space complexity: depends on language and implementation.  Assume O(N) for most cases

if __name__ == '__main__':
    s1 = ['f', 'l', 'u', 's', 't', 'e', 'r']
    s2 = ['r', 'e', 's', 't', 'f', 'u', 'l']

    print(is_anagram(s1, s2))