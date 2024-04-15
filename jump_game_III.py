def canReach( s, minJ, maxJ):
    dp = [c == '0' for c in s]
    pre = 0
    for i in range(1, len(s)):
        if i >= minJ: pre += dp[i - minJ]
        if i > maxJ: pre -= dp[i - maxJ - 1]
        dp[i] &= pre > 0
    return dp[-1]


s = "011010"
minJump = 2
maxJump = 3


canReach(s, minJump, maxJump)