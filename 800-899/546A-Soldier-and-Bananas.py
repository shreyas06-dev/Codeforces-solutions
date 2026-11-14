# 546A - Soldier and Bananas
# Rating: 800
# Approach: in this its a Arithmetic Progression where the D=1 as each is just incrementing by 1
# the approach is to loop to w and then add the k*i values unitl the very end

k, n, w = map(int, input().split())

total = 0
for i in range(w + 1):
    current_price_for_i = k * i
    total = total + current_price_for_i

print(max(0, total - n))