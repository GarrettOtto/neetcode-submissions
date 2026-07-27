class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # To check if string 's' and string 't' are anagrams of each other all we need to do is alphabetize both of them and check if they equal each other
        if ''.join(sorted(s)) == ''.join(sorted(t)):
            return True
        else:
            return False