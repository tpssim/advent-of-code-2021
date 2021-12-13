
# Parse the input from the input file
input_file = 'example_input.txt'
map = {}

with open(input_file) as input:
  for line in input.readlines():
    cave_1, cave_2 = line.rstrip().split('-')
    
    if cave_1 != 'start':
      cave_2_connections = map.get(cave_2, [])
      cave_2_connections.append(cave_1)
      map.update({cave_2: cave_2_connections})

    if cave_2  != 'start':
      cave_1_connections = map.get(cave_1, [])
      cave_1_connections.append(cave_2)
      map.update({cave_1: cave_1_connections})


# Task 1

# Recursive function for finding all possible paths
def find_paths(cave, map, current_path, paths):

  # Add this cave to path
  current_path.append(cave)

  # Stop if at end
  if cave == 'end':
    paths.append(current_path)
    return

  # Go through possible paths
  for c in map.get(cave):
    
    # Cannot visit small cave twice
    if c.islower() and c in current_path:
      continue
    
    # Next recursive step
    else:
      find_paths(c, map, current_path.copy(), paths)

# Find all the paths
paths = []
find_paths('start', map, [], paths)

print(f'Amount of possible paths: {len(paths)}')
print()


# Task 2

# Recursive function for finding all possible paths
def find_paths_2(cave, map, current_path, paths):

  # Add this cave to path
  current_path.append(cave)

  # Stop if at end
  if cave == 'end':
    paths.append(current_path)
    return

  # Go through possible paths
  for c in map.get(cave):

    # 1 small cave can be visited twice
    if c.islower() and c in current_path:

      small_caves = [x for x in current_path if x.islower()]
      
      # Find a possible double visit that already happened
      ok = True
      for small in small_caves:
        if small_caves.count(small) == 2:
          ok = False

      if not ok:
        continue
    
    # Next recursive step
    find_paths_2(c, map, current_path.copy(), paths)

# Find all the paths with the new rule
paths = []
find_paths_2('start', map, [], paths)

print(f'Amount of possible paths with new rule: {len(paths)}')