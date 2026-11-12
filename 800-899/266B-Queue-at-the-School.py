# 266B - Queue at the School
# Rating: 800
# Approach: I first tried to optimise it by  looking at the "t" and simulating it forward, but the problem has a manageable  
# input constraint so no need to optimise
# we do it an iterative way where we swap and move the pointer ahead
n, t = map(int, input().split())
s = list(input().strip())

for _ in range(t):
    i = 0
    while i < n - 1:
        if s[i] == 'B' and s[i + 1] == 'G':
            s[i], s[i + 1] = s[i + 1], s[i]
            i += 2
        else:
            i += 1

print(''.join(s))