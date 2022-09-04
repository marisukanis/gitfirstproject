"""
Cubic dice task:
A cubic dice is rolled. Calculate the probability of throwing more than three if it is known
to have resulted in an even number.

Solution:
Let's introduce the markings:
Ω - one throw of the dice,
A - more than three stitches thrown,
B - An even number of stitches were rolled,
A∩B - An even number of more than 3 stitches is rolled.

We want to calculate the probability of event A, provided that event B happened. We will
use the formula:
P(A|B)=P(A∩B)/P(B)
"""
sigma = (1, 2, 3, 4, 5, 6) #all numbers
A = (4, 5, 6) # only nr over 3
B = (2, 4, 6) # only even numbers rolled

cardinality(sigma) = 6
cardinality(A) = 3
cardinality(B) = 3

A_intersection_B = (4, 6) # even numbers over 3

P = probability

P(A_intersection_B) = cardinality(A_intersection_B) / cardinality(sigma)
P = 2 / 6
P = 1 / 3

P(B) = cardinality(B)/cardinality(sigma)
P = 3 / 6
P = 1 / 2

(1/3) / (1/2) = 2/3 = 66%
