# This year, Santa brought little Bobby Tables a set of wires and bitwise logic gates! Unfortunately, little Bobby is a little under the recommended age range, and he needs help assembling the circuit.
# Each wire has an identifier (some lowercase letters) and can carry a 16-bit signal (a number from 0 to 65535). A signal is provided to each wire by a gate, another wire, or some specific value. Each wire can only get a signal from one source, but can provide its signal to multiple destinations. A gate provides no signal until all of its inputs have a signal.
# The included instructions booklet describes how to connect the parts together: x AND y -> z means to connect wires x and y to an AND gate, and then connect its output to wire z.
# For example:
# 123 -> x means that the signal 123 is provided to wire x.
# x AND y -> z means that the bitwise AND of wire x and wire y is provided to wire z.
# p LSHIFT 2 -> q means that the value from wire p is left-shifted by 2 and then provided to wire q.
# NOT e -> f means that the bitwise complement of the value from wire e is provided to wire f.
# Other possible gates include OR (bitwise OR) and RSHIFT (right-shift). If, for some reason, you'd like to emulate the circuit instead, almost all programming languages (for example, C, JavaScript, or Python) provide operators for these gates.
# For example, here is a simple circuit:
# 123 -> x
# 456 -> y
# x AND y -> d
# x OR y -> e
# x LSHIFT 2 -> f
# y RSHIFT 2 -> g
# NOT x -> h
# NOT y -> i
# After it is run, these are the signals on the wires:
# d: 72
# e: 507
# f: 492
# g: 114
# h: 65412
# i: 65079
# x: 123
# y: 456
# In little Bobby's kit's instructions booklet (provided as your puzzle input), what signal is ultimately provided to wire a?


#Answer: 3176

operations=dict()
results=dict()

with open('07 - Some Assembly Required.txt' ) as txt:
	for line in txt:
		temp=line.split()
		if len(temp)==3:
			if temp[0].isdigit():
				results[temp[2]] = temp[0]
			else:
				operations[temp[2]] = [temp[0]]
		elif len(temp)==4:
			operations[temp[3]]=[temp[0], temp[1]]
		elif len(temp)==5:
			operations[temp[4]]=[temp[0],temp[1],temp[2]]

while len(operations)>0:
	done=list()
	for key1 in results:
		for key2 in operations:
			operations[key2]=[results[key1] if x == key1 else x for x in operations[key2]]

	for key in operations:
		if len(operations[key])==1:
			if operations[key][0].isdigit():
				results[key] = operations[key][0]
				done+=(key,)
		elif operations[key][0] == "NOT":
			if operations[key][1].isdigit():
				results[key]= str(~int(operations[key][1]) & 0xffff)
				done+=(key,)
		elif operations[key][1] == "AND":
			if operations[key][0].isdigit() and operations[key][2].isdigit():
				results[key] = str(int(operations[key][0]) & int(operations[key][2]))
				done+=(key,)
		elif operations[key][1] == "OR":
			if operations[key][0].isdigit() and operations[key][2].isdigit():
				results[key] = str(int(operations[key][0]) | int(operations[key][2]))
				done+=(key,)
		elif operations[key][1] == "RSHIFT":
			if operations[key][0].isdigit():
				results[key]= str(int(operations[key][0]) >> int(operations[key][2]))
				done+=(key,)
		elif operations[key][1] == "LSHIFT":
			if operations[key][0].isdigit():
				results[key] = str(int(operations[key][0]) << int(operations[key][2]))
				done+=(key,)

	for val in done:
		operations.pop(val,None)

print(results['a'])


