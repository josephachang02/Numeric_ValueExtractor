import re

with open('regex_sum.txt', 'r') as file:
    content = file.read()
    values = re.findall('[0-9]+', content)

print(values)
# print values show all the values in a list format. However the strings need to be converted to int

numericValues = [int(value) for value in values]

totalSum = sum(numericValues)

print(totalSum)

