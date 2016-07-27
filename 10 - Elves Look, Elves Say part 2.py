#Now, starting again with the digits in your puzzle input, apply this process 50 times. What is the length of the new result?

#Answer: 6989950

from itertools import groupby

p1 = "1321131112"
for _ in range(50):
	tmp=''
	for k, v in groupby(p1):
		tmp += str(len(list(v))) + k 
	p1=tmp
print(len(p1))