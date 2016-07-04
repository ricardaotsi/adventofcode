# Now find one that starts with six zeroes.

#Answer: 9958218

import hashlib
m="iwrupvqb"
i=0
while(True):
	temp=hashlib.md5(str.encode(m+str(i))).hexdigest()
	if temp[0:6]== "000000":
		break
	i+=1
print(temp)
print(i)