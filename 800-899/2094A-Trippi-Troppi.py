# 2094A - Trippi Troppi
# Rating: 800
# Approach: we first use the split() to get the 3 words individually (i initially was confused and thought that we had to use strip because of the whitespace)
# then we just slice the first letter of each and concatenate them


t = int(input())

for _ in range(t):
    a, b, c = input().split()
    print(a[0] + b[0] + c[0])