import re
text = open('regex_sum_31748.txt')
ls = list()
for line in text:
	line = line.rstrip()
	ls = ls + re.findall('[0-9]+', line)
numbers = list()
for entry in ls:
	numbers.append(int(entry))
total = sum(numbers)
print(len(numbers))
print(total)


