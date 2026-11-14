# 617A - Elephant
# Rating: 800
# Approach: this problem is a greedy problem as we always want to take the maximum number of steps we never want to take less 
# steps than we need . so rather than deciding what number to choose from 1,2,3,4,5 we always choose 5 and work from there 
# we use // and % to process the steps and we use a count to store how many steps were needed

x = int(input())

count = x // 5
rem = x % 5
if rem > 0:
    count = count + 1

print(count)