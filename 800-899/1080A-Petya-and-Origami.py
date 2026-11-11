# 1080A - Petya and Origami
# Rating: 800
# Approach: Each friend needs 2 red, 5 green, 8 blue sheets.
# Total sheets = 2n, 5n, 8n. Each pack has k sheets, so round each
# up to the nearest pack with ceiling division (a + k - 1) // k, then sum.Initially what i thought about was that it should be (color*n)//k but in  case we were short a notebook this wouldnt work at all, so in order to  make it work it would be have to be + (k-1)

n, k = map(int, input().split())

red = (2 * n + k - 1) // k
green = (5 * n + k - 1) // k
blue = (8 * n + k - 1) // k

print(red + green + blue)