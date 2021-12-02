
# Parse the input from the input file
input_file = 'example_input.txt'
readings = []

with open(input_file) as input:
  for line in input.readlines():
    readings.append(int(line))


# Part 1

result = 0
previous = readings[0]

for reading in readings:
  if previous < reading:
    result += 1
  previous = reading

print(f'{result} measurements were larger than the previous one.')
print()


# Part 2

result = 0
previous = readings[0] + readings[1] + readings[2]

for i, reading in enumerate(readings[2:]):
  window = reading + readings[i] + readings[i+1]
  if previous < window:
    result += 1
  previous = window

print(f'{result} measurements were larger than the previous one, when using sliding window filtering.')
  