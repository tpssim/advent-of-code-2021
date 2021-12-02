
# Parse the input from the input file
input_file = 'input.txt'
readings = []

with open(input_file) as input:
  for line in input.readlines():
    reading = line.rstrip().split(' ')
    readings.append([reading[0], int(reading[1])])


# Part 1

horizontal_pos = 0
depth = 0

for reading in readings:
  
  if reading[0] == 'forward':
    horizontal_pos += reading[1]
  
  elif reading[0] == 'down':
    depth += reading[1]

  elif reading[0] == 'up':
    depth -= reading[1]

print(f'After following the planned course our horisontal position will be {horizontal_pos} and depth will be {depth}.')
print(f'Multiplying horizontal position and depth gives {horizontal_pos*depth}.')
print()


# Part 2

horizontal_pos = 0
depth = 0
aim = 0

for reading in readings:
  
  if reading[0] == 'forward':
    horizontal_pos += reading[1]
    depth += aim * reading[1]
  
  elif reading[0] == 'down':
    aim += reading[1]

  elif reading[0] == 'up':
    aim -= reading[1]

print(f'After reading the manual...')
print(f'After following the planned course our horisontal position will be {horizontal_pos} and depth will be {depth}.')
print(f'Multiplying horizontal position and depth gives {horizontal_pos*depth}.')