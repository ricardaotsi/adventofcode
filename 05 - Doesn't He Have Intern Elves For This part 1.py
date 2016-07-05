# Santa needs help figuring out which strings in his text file are naughty or nice.
# A nice string is one with all of the following properties:
# It contains at least three vowels (aeiou only), like aei, xazegov, or aeiouaeiouaeiou.
# It contains at least one letter that appears twice in a row, like xx, abcdde (dd), or aabbccdd (aa, bb, cc, or dd).
# It does not contain the strings ab, cd, pq, or xy, even if they are part of one of the other requirements.
# For example:
# ugknbfddgicrmopn is nice because it has at least three vowels (u...i...o...), a double letter (...dd...), and none of the disallowed substrings.
# aaa is nice because it has at least three vowels and a double letter, even though the letters used by different rules overlap.
# jchzalrnumimnmhp is naughty because it has no double letter.
# haegwjzuvuyypxyu is naughty because it contains the string xy.
# dvszwmarrgswjxmb is naughty because it contains only one vowel.
# How many strings are nice?

#Answer: 238

nice=0
word=""
with open("05 - nice naughty.txt") as txt:
	for line in txt:
		temp=list(line)
		vowels=0
		repetition=False
		contain=False
		for position, i in enumerate(temp):
			if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
				vowels+=1
			if word == i:
				repetition=True
			if word+i == "ab" or word+i == "cd" or word+i == "pq" or word+i == "xy":
				contain=True
			word = i
		if vowels>=3 and repetition and not contain:
			nice+=1
print(nice)