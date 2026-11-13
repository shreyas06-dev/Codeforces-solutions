# 1A - Theatre Square
# Rating: 800
# Approach: This problem  is similar in concept to the one i solved in the Petya and origami question
# the way it  works is that , we have a place of n x m dimension and square of dimension a x a and we have to fill the square
# similar to the petya and origami question we have ot use a math ceiling concept 
# rather than using the math function , i just used the numerical equivalent of if because i cant remember the function name when solving it.

n, m, a = map(int, input().split())

print(((n + a - 1) // a) * ((m + a - 1) // a))