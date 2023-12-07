# project euler - problem 684

def fibonacci(i, memo={0: 0, 1: 1}):
    if i in memo.keys():
        return memo[i], memo
    else:
        ans = fibonacci(i - 1, memo)[0] + fibonacci(i - 2, memo)[0]
        memo[i] = ans
        return ans, memo


fibs = list(fibonacci(90)[1].values())[2:]
print(fibs)


def s(n):
    return
