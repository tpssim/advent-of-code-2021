
# Parse the input from the input file
input_file = 'example_input.txt'
inputs = []
outputs = []

with open(input_file) as input:
  for line in input.readlines():
    split_line = line.split(' | ')

    # Sort every string alphabetically to make further analysis easier
    inputs.append([''.join(sorted(digit)) for digit in split_line[0].split()])
    outputs.append([''.join(sorted(digit)) for digit in split_line[1].split()])


# Task 1

# Count the digits 1, 4, 7 and 8 in all outputs
# (They use 2, 4, 3 and 7 segments respectively)
count = 0

for output in outputs:
  for digit in output:
    if len(digit) in {2, 4, 3, 7}:
      count += 1

print(f'Digits 1, 4, 7 and 8 appear {count} times in the output values.')
print()


# Task 2

# Decode every output into a 4 digit number
decoded_outputs = [0] * len(outputs)

for i, input in enumerate(inputs): 

  # Index of a sequence in decode_key will tell the number that sequence represents
  decode_key = [''] * 10

  # First the obivous ones (1, 4, 7, 8)
  decode_key[1] = [digit for digit in input if len(digit) == 2][0]
  decode_key[4] = [digit for digit in input if len(digit) == 4][0]
  decode_key[7] = [digit for digit in input if len(digit) == 3][0]
  decode_key[8] = [digit for digit in input if len(digit) == 7][0]

  # 3 is only one with length of 5 and containing both segments of 1
  decode_key[3] = ([digit for digit in input if len(digit) == 5 and 
                  all([decode_key[1][0] in digit, decode_key[1][1] in digit])][0])

  # 6 is only one with length of 6 and not containing all segments of 7
  decode_key[6] = ([digit for digit in input if len(digit) == 6 and 
                  not all([decode_key[7][0] in digit,
                          decode_key[7][1] in digit,
                          decode_key[7][2] in digit])
                  ][0])

  # 9 is only one with length of 6 and containing all segments of 3
  decode_key[9] = ([digit for digit in input if len(digit) == 6 and 
                  all([decode_key[3][0] in digit, 
                      decode_key[3][1] in digit,
                      decode_key[3][2] in digit,
                      decode_key[3][3] in digit,
                      decode_key[3][4] in digit])
                  ][0])

  # 5 is only one that shares all its segments with 6
  decode_key[5] = ([digit for digit in input if len(digit) == 5 and
                  all([digit[0] in decode_key[6],
                      digit[1] in decode_key[6],
                      digit[2] in decode_key[6],
                      digit[3] in decode_key[6],
                      digit[4] in decode_key[6]])
                  ][0])

  # 2 is the remaining one with length 5
  decode_key[2] = [digit for digit in input if len(digit) == 5 and digit not in decode_key][0]

  # 0 is the remaining one
  decode_key[0] = [digit for digit in input if digit not in decode_key][0]
  
  # Use the decode key to decode the outputs
  decoded_outputs[i] = int(''.join([str(decode_key.index(digit)) for digit in outputs[i]]))


# Sum of all decoded outputs
output_sum = sum(decoded_outputs)

print(f'Sum of all decoded output values is {output_sum}.')