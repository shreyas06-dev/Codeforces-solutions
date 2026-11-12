# 1360A - Minimal Square
# Rating: 800
# Approach: OK so this took me a little bit to figure out and it wasnt all that straight forward 
# so i figured that we needed to divided the smaller number of the input by the bigger
# if it is divisible we just square the bigger number as is and thats the answer
# if it is not divisible we just add 1 to the bigger number and square it

t = int(input())

for _ in range(t):
    a, b = map(int, input().split())

    side = min(max(2 * a, b), max(2 * b, a))
    area = side * side
    print(area)