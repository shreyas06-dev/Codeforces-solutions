# 1030A - In Search of an Easy Problem
# Rating: 800
# Approach: this is very straight forward. if 1 exists in the input its "HARD"
# else its "EASY". this was very simple

n = int(input())
x = list(map(int, input().split()))

if 1 in x:
    print("HARD")
else:
    print("EASY")