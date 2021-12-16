
# Parse the input from the input file
input_file = 'example_input.txt'
map = []

with open(input_file) as input:
  for line in input.readlines():
    map.append([int(x) for x in line.rstrip()])


# Return the key with the smallest value in a dictionary
def getSmallest(dict):
  return min(dict, key=dict.get)

# Return a risk of given position in a map
def getRisk(map, pos):
  return map[pos[1]][pos[0]]

# Find the risk of optimal route from start to stop on map (Djikstras algorithm)
def optimalRoute(map, start, stop, x_max, y_max):

  x, y = start
  queue = {(x, y+1): getRisk(map, (x, y+1)), (x+1, y): getRisk(map, (x+1, y))}
  visited = [start]

  while True:

    x, y = getSmallest(queue)
    risk = queue.pop((x, y))

    if (x, y) == stop:
      break
    
    visited.append((x, y))

    left = (x-1, y)
    rigth = (x+1, y)
    up = (x, y-1)
    down = (x, y+1)

    if x != 0 and left not in visited:
      if queue.get(left, float('inf')) > risk + getRisk(map, left):
        queue.update({left: risk + getRisk(map, left)})

    if x != x_max and rigth not in visited:
      if queue.get(rigth, float('inf')) > risk + getRisk(map, rigth):
        queue.update({rigth: risk + getRisk(map, rigth)})

    if y != 0 and up not in visited:
      if queue.get(up, float('inf')) > risk + getRisk(map, up):
        queue.update({up: risk + getRisk(map, up)})

    if y != y_max and down not in visited:
      if queue.get(down, float('inf')) > risk + getRisk(map, down):
        queue.update({down: risk + getRisk(map, down)})

  return risk


# Task 1

# Find the bottom corner
x_max = len(map[0]) - 1
y_max = len(map) - 1

# Get the risk of optimal route
optimal_route = optimalRoute(map, (0, 0), (x_max, y_max), x_max, y_max)

print(f'Total risk of optimal path: {optimal_route}')
print()


# Task 2

print('This might take a while...')

# Generate the full map
new_map = [line.copy() for line in map]

# Extend left
for y, line in enumerate(map):

  for i in range(4):
    
    new_map[y].extend([(risk+i) % 9 + 1 for risk in line])

# Extend down
copy = new_map.copy()
for i in range(4):
  for x, line in enumerate(copy):

    y = len(map) + (len(map) * i) + x
    new_map.insert(y, [(risk+i) % 9 + 1 for risk in line])


# Find the bottom corner
x_max = len(new_map[0]) - 1
y_max = len(new_map) - 1

# Get the risk of optimal route
optimal_route = optimalRoute(new_map, (0, 0), (x_max, y_max), x_max, y_max)

print(f'Total risk of optimal path with the full map: {optimal_route}')