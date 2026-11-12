# 96A - Football
# Rating: 800
# Approach: just see if 7 consecutive 0's or 1's exist
# initially i thought about counting continuous elements but that seemed like too much for such a simple approach

s = input().strip()

if "0000000" in s or "1111111" in s:
    print("YES")
else:
    print("NO")