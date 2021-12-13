
# Parse the input from the input file
input_file = 'example_input.txt'
dots = []
folds = []

with open(input_file) as input:
  for line in input.readlines():
    
    if line == '\n':
      continue

    elif line.startswith('fold'):
      dir, val = line.rstrip().strip('fold along ').split('=')
      folds.append((dir, int(val)))

    else:
      x, y = line.rstrip().split(',')
      dots.append((int(x), int(y)))

# Fold a paper(list[y][x]) along given line 
def fold(paper, direction, position):

  # Vertical fold
  if direction == 'x':

    left_half = [line[:position] for line in paper]
    rigth_half = [line[position+1:] for line in paper]
    rigth_half = [line[::-1] for line in rigth_half]

    for y, line in enumerate(rigth_half):
      for x, pos in enumerate(line):

        if pos == '#':
          left_half[y][x] = '#'

    return left_half

  # Horizontal fold
  elif direction == 'y':

    top_half = paper[:position]
    bottom_half = paper[position+1:]
    bottom_half.reverse()

    for y, line in enumerate(bottom_half):
      for x, pos in enumerate(line):

        if pos == '#':
          top_half[y][x] = '#'

    return top_half


# Task 1 

# Find boundaries
x_max = max([x for x, y in dots])
y_max = max([y for x, y in dots])

# Create the paper
paper = [ ['.' for _ in range(x_max+1)] for _ in range(y_max+1) ]

# Add the dots
for x, y in dots:
  paper[y][x] = '#'

# Fold once
folded = fold(paper, folds[0][0], folds[0][1])

# Count dots
dot_count = 0
for line in folded:
  dot_count += line.count('#')

print(f'After one fold the paper has {dot_count} dots.')
print()


# Task 2

folds.pop(0)

# Finish folding
for dir, pos in folds:
  folded = fold(folded, dir, pos)


# See the result
print('Paper after folding:')

for line in folded:
  print(line)