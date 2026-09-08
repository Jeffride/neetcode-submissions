class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Order doesn't matter for anagram
        if len(s) != len(t):
            return False

        s,t = str("".join(sorted(s))),str("".join(sorted(t)))        

        if s == t:
            return True
        return False