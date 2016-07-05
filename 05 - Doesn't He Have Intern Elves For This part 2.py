# Realizing the error of his ways, Santa has switched to a better model of determining whether a string is naughty or nice. None of the old rules apply, as they are all clearly ridiculous.
# Now, a nice string is one with all of the following properties:
# It contains a pair of any two letters that appears at least twice in the string without overlapping, like xyxy (xy) or aabcdefgaa (aa), but not like aaa (aa, but it overlaps).
# It contains at least one letter which repeats with exactly one letter between them, like xyx, abcdefeghi (efe), or even aaa.
# For example:
# qjhvhtzxzqqjkmpb is nice because is has a pair that appears twice (qj) and a letter that repeats with exactly one letter between them (zxz).
# xxyxx is nice because it has a pair that appears twice and a letter that repeats with one between, even though the letters used by each rule overlap.
# uurcxstgmygtbstg is naughty because it has a pair (tg) but no repeat with a single letter between them.
# ieodomkazucvgmuy is naughty because it has a repeating letter with one between (odo), but no pair that appears twice.
# How many strings are nice under these new rules?

#Answer: 69

nice=0
with open("05 - nice naughty.txt") as txt:
	for line in txt:
		letterrepeat=False
		for i in range(0,len(line)-2):
			if line[i] == line[i+2]:
				letterrepeat = True
				break
		pair=False
		for i in range(0,len(line)-1):
			if line.count(line[i]+line[i+1])>1:
				pair=True
				break
		if letterrepeat and pair:
			nice+=1
print(nice)