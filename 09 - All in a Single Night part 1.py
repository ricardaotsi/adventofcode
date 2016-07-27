#Every year, Santa manages to deliver all of his presents in a single night.
# This year, however, he has some new locations to visit; his elves have provided him the distances between every pair of locations. He can start and end at any two (different) locations he wants, but he must visit each location exactly once. What is the shortest distance he can travel to achieve this?
# For example, given the following distances:
# London to Dublin = 464
# London to Belfast = 518
# Dublin to Belfast = 141
# The possible routes are therefore:
# Dublin -> London -> Belfast = 982
# London -> Dublin -> Belfast = 605
# London -> Belfast -> Dublin = 659
# Dublin -> Belfast -> London = 659
# Belfast -> Dublin -> London = 605
# Belfast -> London -> Dublin = 982
# The shortest of these is London -> Dublin -> Belfast = 605, and so the answer is 605 in this example.
# What is the distance of the shortest route?

#Answer: 251

from itertools import permutations
from collections import defaultdict

city=set()
path = defaultdict(dict)
with open('09 - All in a Single Night.txt' ) as txt:
	for line in txt:
		temp = line.split()
		city.add(temp[0])
		city.add(temp[2])
		path[temp[0]][temp[2]] = int(temp[4])
		path[temp[2]][temp[0]] = int(temp[4])
dist=list()
for row in permutations(city):
	dist.append(sum(map(lambda x, y: path[x][y],row[:-1],row[1:])))
print(min(dist))

