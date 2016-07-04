# The elves are also running low on ribbon. Ribbon is all the same width, so they only have to worry about the length they need to order, which they would again like to be exact.
# The ribbon required to wrap a present is the shortest distance around its sides, or the smallest perimeter of any one face. Each present also requires a bow made out of ribbon as well; the feet of ribbon required for the perfect bow is equal to the cubic feet of volume of the present. Don't ask how they tie the bow, though; they'll never tell.
# For example:
# A present with dimensions 2x3x4 requires 2+2+3+3 = 10 feet of ribbon to wrap the present plus 2*3*4 = 24 feet of ribbon for the bow, for a total of 34 feet.
# A present with dimensions 1x1x10 requires 1+1+1+1 = 4 feet of ribbon to wrap the present plus 1*1*10 = 10 feet of ribbon for the bow, for a total of 14 feet.
# How many total feet of ribbon should they order?

#Answer: 3812909

lista=list()
pm=int()
with open('02 - presentsize.txt') as txt:
	for line in txt:
		primeiro,segundo,terceiro=line.split("x")
		lista.append([int(primeiro),int(segundo),int(terceiro)])
for i in lista:
	p1=sorted(i)[0]
	p2=sorted(i)[1]
	p3=sorted(i)[2]
	pm+=2*p1+2*p2+p1*p2*p3
print(pm)
	