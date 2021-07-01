"""Solution for Triple Step by Bhavjot Grewal, from Chapter 8, pg. 134 of CCTI."""


def triple_step(n: int) -> int:
    """A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.\
    Implement a method to count how many possible ways the child can run up the stairs.
    """

    # Note: This is similar to the counting stairs problem on leetcode.

    # Dynamic programming can be used (bottom-up) to reach the correct solution.

    if n < 3:
        return n

    dp = [1] * (n + 1)

    dp[0] = 0
    dp[1] = 1
    dp[2] = 2
    dp[3] = 4

    for i in range(4, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]

    return dp[n]