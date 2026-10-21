
class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)

        if all(s[i] <= s[i + 1] for i in range(n - 1)):
            return 0

        if n == 2:
            return -1

        if s[0] == max(s) and s[-1] == min(s):
            if n == 3:
                return 2 if s[0] == s[1] or s[1] == s[-1] else 3
            return 2 if s.count(s[0]) > 1 or s.count(s[-1]) > 1 else 3

        if s[0] == min(s) or s[-1] == max(s):
            return 1

        return 2
