# The next year, just to show off, Santa decides to take the route with the longest distance instead.
# He can still start and end at any two (different) locations he wants, and he still must visit each location exactly once.
# For example, given the distances above, the longest route would be 982 via (for example) Dublin -> London -> Belfast.
# What is the distance of the longest route?

#Answer: 898

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
print(max(dist))

