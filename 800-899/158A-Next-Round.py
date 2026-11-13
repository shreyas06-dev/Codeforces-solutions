# 158A - Next Round
# Rating: 800
# Approach: THIS was fairly easy but i did run into an error becuase i didnt read the question properlyon  a test case
# my initial submission was rejected  for a test case of 0,0,0,0 
n, k = map(int, input().split())
scores = list(map(int, input().split()))

count = 0
for i in range(n):
    if scores[i] >= scores[k - 1] and scores[i] > 0:
        count = count + 1

print(count)