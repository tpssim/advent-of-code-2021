
# Parse the input from the input file
input_file = 'example_input.txt'
lines = []

with open(input_file) as input:
  for line in input.readlines():
    lines.append(line.rstrip())


# Task 1

# Find syntax errors and score them
err_score = 0
scoring = {')': 3, ']': 57, '}': 1197, '>': 25137}

open = ['(', '[', '{', '<']
close = [')', ']', '}', '>']

for line in lines:

  # Queue of expected closing characters
  expected = []

  for char in line:

    # For opening caracter add the corresponding closing character to queue
    if char in open:
      expected.append(close[open.index(char)])

    # For closing character check if expected, if not score the error and continue to next line
    else:
      if char == expected.pop():
        continue
      else:
        err_score += scoring.get(char)
        break

print(f'Syntax error score of all errors: {err_score}')
print()


# Task 2

# Find incomlete lines and score the completons
complete_scores = []
scoring = {')': 1, ']': 2, '}': 3, '>': 4}

for line in lines:

  # Queue of expected closing characters
  expected = []
  err = False

  for char in line:

    # For opening caracter add the corresponding closing character to queue
    if char in open:
      expected.append(close[open.index(char)])

    # For closing character check if expected, if not ignore the line
    else:
      if char == expected.pop():
        continue
      else:
        err = True
        break

  if not err:

    complete_score = 0
    expected.reverse()

    for char in expected:
      complete_score = (complete_score * 5) + scoring.get(char)

    complete_scores.append(complete_score)

# Find the middle complete score
complete_scores.sort()
complete_score = complete_scores[int(len(complete_scores) / 2)] 

print(f'Middle complete score: {complete_score}')