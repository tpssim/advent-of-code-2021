
# Parse the input from the input file
input_file = 'example_input.txt'
polymer_template = ''
rules = {}

with open(input_file) as input:

  # Template line
  polymer_template = input.readline().rstrip()

  # Empty line
  input.readline()

  # Rest is rules
  for line in input.readlines():
    
    pair, insert = line.rstrip().split(' -> ')
    rules.update({pair: insert})


# Do a pair insertion 
def pairInsert(polymer, rules):
  
  # Using a list instead of a string is faster but uses more memory
  result = [polymer[0]]

  for i, second in enumerate(polymer[1:]):
    first = polymer[i]
    pair = first + second

    # Get elemet to be inserted from rules
    insert = rules.get(pair)

    # Add to result
    result.extend([insert, second])

  return ''.join(result)


# Task 1

# Do 10 pair insertions
polymer = polymer_template
for i in range(10):
  polymer = pairInsert(polymer, rules)

# Find every unique element of the result polymer
unique_elemets = set(polymer)

# Count every unique elemet
counts = {}
for element in unique_elemets:
  count = polymer.count(element)
  counts.update({element: count})

# Find most and least common elements
most_common = max(counts, key=counts.get)
least_common = min(counts, key=counts.get)

substracted = counts.get(most_common) - counts.get(least_common)

print(f'After 10 pair insertions the most common element is {most_common} and the least common element is {least_common}.')
print(f'Substracting the amount of least common elements from the amount of most common elements produces {substracted}.')
print()


# Task 2
# This method is not very efficint but it get the job ton in reasonable amount of time

print('This takes a moment')
print()

# Do multiple consecutive inserts for a single pair of elements
# Add the count of each element to counts after the inserts
def multiPairInsert(pair, rules, counts, inserts):

  # Do inserts for one pair at a time
  part_result = pair
  for i in range(inserts):
    part_result = pairInsert(part_result, rules)

  # Remove duplicate
  part_result = part_result[:-1]

  # Find every unique element of the part result polymer
  unique_elemets = set(part_result)

  # Add to count
  for element in unique_elemets:
    count = part_result.count(element) + counts.get(element, 0)
    counts.update({element: count})


# Do 10 more pair insertions
for i in range(10):
  polymer = pairInsert(polymer, rules)

# Get counts for each pair after 20 more insertions
pair_counts = {}
for pair in rules.keys():
  pair_count = {}

  multiPairInsert(pair, rules, pair_count, 20)

  pair_counts.update({pair: pair_count})

# Add counts
# Last element of the epolumer needs to be added manully here 
counts = {polymer[-1]: 1}
for index, second in enumerate(polymer[1:]):
  first = polymer[index]
  pair = first + second

  for element, value in pair_counts.get(pair).items():
    count = value + counts.get(element, 0)
    counts.update({element: count})

# Find most and least common elements
most_common = max(counts, key=counts.get)
least_common = min(counts, key=counts.get)

substracted = counts.get(most_common) - counts.get(least_common)

print(f'After 40 pair insertions the most common element is {most_common} and the least common element is {least_common}.')
print(f'Substracting the amount of least common elements from the amount of most common elements produces {substracted}.')