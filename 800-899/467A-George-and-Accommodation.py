# 467A - George and Accommodation
# Rating: 800
# Approach: Very easy problem, p is how many people are in the room, q is the total capacity
# we need a room where george and his friend can stay, ie a room in which q-p>=2, as we find the room we increase the count

n = int(input())

count = 0
for _ in range(n):
    p, q = map(int, input().split())
    
    if q - p >= 2:
        count = count + 1

print(count)