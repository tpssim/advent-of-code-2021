
# Parse the input from the input file
input_file = 'example_input.txt'
lines = []

with open(input_file) as input:
  for line in input.readlines():
    line = line.rstrip().split(' -> ')
    lines.append([line[0].split(','), line[1].split(',')])


# Map containing the vent positions
class Map():

  # Init a map with size from (0, 0) to (x_max, y_max)
  def __init__(self, x_max, y_max):
    self.map = [ [0 for _ in range(x_max+1)] for _ in range(y_max+1) ]


  # Add line of vent to the map
  def addLine(self, line, consider_diagonal=True):
    x1 = int(line[0][0])
    y1 = int(line[0][1])
    x2 = int(line[1][0])
    y2 = int(line[1][1])

    # Vertical line
    if x1 == x2:
      x = x1
      y_range = range(y1, y2+1) if y1 < y2 else range(y2, y1+1)

      for y in y_range:
        self.map[y][x] += 1
      
      return

    # Horizontal line
    if y1 == y2:
      y = y1
      x_range = range(x1, x2+1) if x1 < x2 else range(x2, x1+1)

      for x in x_range:
        self.map[y][x] += 1
      
      return

    # Diagonal line(always 45 degrees)
    if consider_diagonal:
      x_range = range(x1, x2+1) if x1 < x2 else range(x1, x2-1, -1)
      y_range = range(y1, y2+1) if y1 < y2 else range(y1, y2-1, -1)
      
      for i, x in enumerate(x_range):
        y = y_range[i]
        self.map[y][x] += 1

      return
      

  # Count points on the map that have a value bigger than val
  def countPointsBiggerThan(self, val):
    count = 0
    
    for x in self.map:
      count += sum(1 for y in x if y > val)
    
    return count
  

  # Print the map to console
  def printMap(self):
    for line in self.map:
      print(*line)


# Task 1

x_max = 0
y_max = 0

# Find map boundaries
for line in lines:
  x1 = int(line[0][0])
  y1 = int(line[0][1])
  x2 = int(line[1][0])
  y2 = int(line[1][1])

  line_x_max = x1 if x1 > x2 else x2
  line_y_max = y1 if y1 > y2 else y2

  if x_max < line_x_max:
    x_max = line_x_max

  if y_max < line_y_max:
    y_max = line_y_max

# Init map
map = Map(x_max, y_max)

# Add horizontal and vertical lines to the map
for line in lines:
  map.addLine(line, consider_diagonal=False)

print('Mapping vertical and horizontal lines only')

# Bad idea. The actual input is too big for this to look pretty.
#map.printMap()
#print()
print(f'Count of Points in the map with 2 or more vents: {map.countPointsBiggerThan(1)}')
print()


# Task 2

# Init map again. Reuse boundaries found in task 1.
map = Map(x_max, y_max)

# Add all lines to the map
for line in lines:
  map.addLine(line)

print('Mapping all lines')
print(f'Count of Points in the map with 2 or more vents: {map.countPointsBiggerThan(1)}')