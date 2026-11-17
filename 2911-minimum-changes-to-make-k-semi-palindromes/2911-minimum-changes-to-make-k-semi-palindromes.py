
class Solution:
    def minimumChanges(self, s: str, k: int) -> int:
        n = len(s)
        INF = float('inf')

        # Precompute cost of making every substring
        # a semi-palindrome.
        cost = [[0] * n for _ in range(n)]

        for l in range(n):
            for r in range(l + 1, n):
                length = r - l + 1
                best = INF

                for d in range(1, length):
                    if length % d != 0:
                        continue

                    changes = 0

                    # Each group contains indices with
                    # the same remainder modulo d.
                    for t in range(d):
                        group_len = (length - 1 - t) // d + 1

                        for x in range(group_len // 2):
                            i = l + t + x * d
                            j = l + t + (group_len - 1 - x) * d

                            if s[i] != s[j]:
                                changes += 1

                    best = min(best, changes)

                cost[l][r] = best

        # DP: first i characters divided into p parts.
        dp = [[INF] * (k + 1) for _ in range(n + 1)]
        dp[0][0] = 0

        for p in range(1, k + 1):
            for i in range(2 * p, n + 1):

                for j in range(2 * (p - 1), i - 1):
                    dp[i][p] = min(
                        dp[i][p],
                        dp[j][p - 1] + cost[j][i - 1]
                    )

        return dp[n][k]
