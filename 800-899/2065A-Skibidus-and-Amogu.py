# 2065A - Skibidus and Amog'u
# Rating: 800
# Approach: The singular form ends with "us", and the plural form replaces the "us" with "i".
# we need to use string slicing to remove the us and add the i.

t = int(input())
for _ in range(t):
    s = input().strip()
    print(s[:-2] + "i")