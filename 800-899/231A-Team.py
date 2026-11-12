# 231A - Team
# Rating: 800
# Approach: For this i just checked if any two combination
# of friends both have 1, if so increases count
# Another approach for this would be to add the numbers of the 
# friends and see if their total is equal to or greater than 2
# sum(friends)>=2

# also i learned that its "and" and not "&"
# the former is logical and the latter is bitwise

n = int(input())
count = 0

for _ in range(n):
    a, b, c = map(int, input().split())

    if (a == 1 and b == 1) or (a == 1 and c == 1) or (b == 1 and c == 1):
        count = count + 1

print(count)