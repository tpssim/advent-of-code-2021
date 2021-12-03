
# Parse the input from the input file
input_file = 'example_input.txt'
readings = []

with open(input_file) as input:
  for line in input.readlines():
    readings.append(list(line.rstrip()))


# Part 1

def cnt(input, index):
  count = 0
  for number in input:
    if number[index] == '1':
      count += 1
    elif number[index] == '0':
      count -= 1
  return count

counts = [0] * len(readings[0])

for i in range(len(counts)):
  counts[i] = cnt(readings, i)

gamma_rate = ''

for count in counts:
  if count > 0:
    gamma_rate = gamma_rate + '1'
  elif count < 0:
    gamma_rate = gamma_rate + '0'

epsilon_rate = gamma_rate.replace('1', '2').replace('0', '1').replace('2', '0')

power_consumption = (int(gamma_rate, 2)) * (int(epsilon_rate, 2))

print(f'Gamma rate: {gamma_rate}')
print(f'Epsilon rate: {epsilon_rate}')
print(f'Power consumption: {power_consumption}')


# Part 2

oxygen_generator_rating = readings.copy()

bit = 0
while len(oxygen_generator_rating) > 1:
  count = cnt(oxygen_generator_rating, bit)
  remove = '1' if count < 0 else '0'
  
  oxygen_generator_rating = [number for number in oxygen_generator_rating if not number[bit] == remove]

  bit += 1

oxygen_generator_rating = ''.join(oxygen_generator_rating[0])


CO2_scrubber_rating = readings.copy()

bit = 0
while len(CO2_scrubber_rating) > 1:
  count = cnt(CO2_scrubber_rating, bit)
  remove = '1' if count >= 0 else '0'
  
  CO2_scrubber_rating = [number for number in CO2_scrubber_rating if not number[bit] == remove]

  bit += 1

CO2_scrubber_rating = ''.join(CO2_scrubber_rating[0])


life_support_rating = (int(oxygen_generator_rating, 2)) * (int(CO2_scrubber_rating, 2))

print(f'Oxygen generator rating: {oxygen_generator_rating}')
print(f'CO2 scrubber rating: {CO2_scrubber_rating}')
print(f'Life support rating: {life_support_rating}')