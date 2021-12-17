
# Parse the input from the input file
input_file = 'example_input.txt'
target_x = ''
target_y = ''

with open(input_file) as input:
  line = input.readline().rstrip()
  line = line[15:]

  target_x, target_y = line.split(', y=')

  target_x = tuple([int(x) for x in target_x.split('..')])
  target_y = tuple([int(y) for y in target_y.split('..')])


# Task 1

# Test if point is in target area
def testHit(point):
  
  x, y = point
  return x >= target_x[0] and x <= target_x[1] and y >= target_y[0] and y <= target_y[1]

# Simulate shot with velcity. Return coordinates of the hit and highes point of trajectory if target is hit
# Return false if target is missed
def simulateShot(velocity):
  
  x, y = velocity
  x_vel, y_vel = velocity
  highest_point = 0
  
  # While not gone past the target
  while x <= target_x[1] and y >= target_y[0]:
    
    # Update highes point
    highest_point = max(y, highest_point) 

    if testHit((x, y)):

      return {'hit': (x, y), 'highest_point': highest_point}

    # Update velocities
    if x_vel > 0:
      x_vel -= 1
    elif x_vel < 0:
      x_vel += 1
    y_vel -= 1

    # Update x and y
    x += x_vel
    y += y_vel

  return False


hits = []

# Simulate some shots
# Any value that overshoots the far corner of the target does not need to be tested
for x in range(target_x[1] + 1):

  for y in range(target_y[0], abs(target_y[0])):

    hit = simulateShot((x,y))

    if hit:
      hit.update({'initial_velocity': (x, y)})

      hits.append(hit)

# Find the shot with highest point
highest_point = max([hit.get('highest_point') for hit in hits])

print(f'Highest y point a trajectory that hits the target can have is: {highest_point}.')


# Task 2
count = len(hits)

print(f'There is {count} possible initial velocities that will provide a hit.')