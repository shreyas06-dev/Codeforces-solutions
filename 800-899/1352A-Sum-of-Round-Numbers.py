# 1352A - Sum of Round Numbers
# Rating: 800
# Approach: This took me a little bit of time to really understand on hwo to do it
# so the approach is similar to how we would do it for a reversing a number (% ,//) 

t = int(input())

for _ in range(t):
    n = int(input())
    parts = []
    place = 1

    while n > 0:
        digit = n % 10
        if digit != 0:
            parts.append(digit * place)
        n = n // 10
        place = place * 10

    print(len(parts))
    print(' '.join(map(str, parts)))