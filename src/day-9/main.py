
# Parse the input from the input file
input_file = 'example_input.txt'
map = []

with open(input_file) as input:
  for line in input.readlines():
    map.append([int(num) for num in line.rstrip()])


# Task 1

# store low points as tuples (x, y, risk level)
low_points = []

for y, row in enumerate(map):
  for x, heigth in enumerate(row):

    low_point = True

    # Up
    if y != 0 and heigth >= map[y-1][x]:
      low_point = False

    # Down
    try:
      if heigth >= map[y+1][x]:
        low_point = False
    except:
      pass

    # Left
    if x != 0 and heigth >= map[y][x-1]:
      low_point = False  

    # Rigth
    try:
      if heigth >= map[y][x+1]:
        low_point = False
    except:
      pass

    if low_point:
      low_points.append((x, y, heigth+1))

risk_level_sum = sum([point[2] for point in low_points])

print(f'Sum of risk levels off all low points is {risk_level_sum}.')
print()


# Task 2

# Find the basin size for each low point
basins = []

for low_point in low_points:

  # Points (x, y) in the basin
  basin = [(low_point[0], low_point[1])]

  done = False
  while not done:

    new_points = []
    for point in basin:
      
      # Adjacent points
      up = (point[0], point[1] - 1) if point[1] > 0 else None
      down = (point[0], point[1] + 1) if point[1] < len(map) - 1  else None
      left = (point[0] - 1, point[1]) if point[0] > 0 else None
      rigth = (point[0] + 1, point[1]) if point[0] < len(map[0]) - 1 else None

      # Find points not already in basin or in new_points
      if up and up not in basin and up not in new_points:
        if map[up[1]][up[0]] != 9:
          new_points.append(up)

      if down and down not in basin and down not in new_points:
        if map[down[1]][down[0]] != 9: 
          new_points.append(down)

      if left and left not in basin and left not in new_points:
        if map[left[1]][left[0]] != 9:
          new_points.append(left)

      if rigth and rigth not in basin and rigth not in new_points:
        if map[rigth[1]][rigth[0]] != 9:         
          new_points.append(rigth)

    # Add 
    if len(new_points) > 0:
      basin.extend(new_points)
    else:
      done = True

  basins.append(len(basin))


# Find 3 largest basins
largest_basins = []
for i in range(3):
  largest_basins.append(basins.pop(basins.index(max(basins))))

print(f'Size of the 3 lasrgest basins multiplied together is {largest_basins[0] * largest_basins[1] * largest_basins[2]}.')