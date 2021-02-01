class Solution:
    def dfs(self, n, visit, cnt):
        if (cnt == n + 1):
            return 1
        ret = 0
        for i in range(1, n + 1):
            if (not visit[i] and (i % cnt == 0 or cnt % i == 0)):
                visit[i] = 1
                ret += self.dfs(n, visit, cnt + 1)
                visit[i] = 0
        return ret;
    def countArrangement(self, n: int) -> int:
        visit = [0] * (n + 1)
        return self.dfs(n, visit, 1)
