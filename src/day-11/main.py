
# Parse the input from the input file
input_file = 'example_input.txt'
octopi = []

with open(input_file) as input:
  for line in input.readlines():
    octopi.append([int(num) for num in line.rstrip()])


# Task 1

flash_count = 0

# Simulate 100 steps
for i in range(100):

  # List of octopi already flashed during this step as (x, y) tuples
  flashed = []
  step_done = False

  while not step_done:

    # Octopi that will flash during this iteration
    will_flash = []

    for y, row in enumerate(octopi):

      for x, charge in enumerate(row): 

        # Skip if already flashed during this step
        if (x, y) in flashed:
          continue
        
        # Check if ready to flash
        if charge >= 9: 
          will_flash.append((x, y))

    # Check if any octopi will flash
    if will_flash == []:
      step_done = True

    # Charge increments caused by the flashes
    else:

      for flash_x, flash_y in will_flash:

        # Go through adjacent octopi
        for x in range(max(flash_x - 1, 0), min(flash_x + 2, len(octopi[0]))):

          for y in range(max(flash_y - 1, 0), min(flash_y + 2, len(octopi))):

            # Ignore the flashing octopus and all octopi already flashed
            if not ( (x, y) == (flash_x, flash_y) or (x, y) in flashed or (x, y) in will_flash ):
              octopi[y][x] += 1

        # Set charge to 0 after flash
        octopi[flash_y][flash_x] = 0

      # Add newly flashed octopi in flashed
      flashed.extend(will_flash)

  # Add every flash to flash count
  flash_count += len(flashed)

  # Increment the charge of every octopus that did not flash
  for y in range(len(octopi)):
      for x in range(len(octopi[0])):
        if (x, y) not in flashed:
          octopi[y][x] += 1


print(f'After 100 steps {flash_count} flashes occurred.')
print()


# Task 2

# Use the same loop as in part 1, just simulate until all octopi flash simultaneously
step = 100
done = False

while not done:

  # List of octopi already flashed during this step as (x, y) tuples
  flashed = []
  step_done = False
  step += 1

  while not step_done:

    # Octopi that will flash during this iteration
    will_flash = []

    for y, row in enumerate(octopi):

      for x, charge in enumerate(row): 

        # Skip if already flashed during this step
        if (x, y) in flashed:
          continue
        
        # Check if ready to flash
        if charge >= 9: 
          will_flash.append((x, y))

    # Check if any octopi will flash
    if will_flash == []:
      step_done = True

    # Charge increments caused by the flashes
    else:

      for flash_x, flash_y in will_flash:

        # Go through adjacent octopi
        for x in range(max(flash_x - 1, 0), min(flash_x + 2, len(octopi[0]))):

          for y in range(max(flash_y - 1, 0), min(flash_y + 2, len(octopi))):

            # Ignore the flashing octopus and all octopi already flashed
            if not ( (x, y) == (flash_x, flash_y) or (x, y) in flashed or (x, y) in will_flash ):
              octopi[y][x] += 1

        # Set charge to 0 after flash
        octopi[flash_y][flash_x] = 0

      # Add newly flashed octopi in flashed
      flashed.extend(will_flash)

  # Add every flash to flash count
  flash_count += len(flashed)

  # Increment the charge of every octopus that did not flash
  for y in range(len(octopi)):
      for x in range(len(octopi[0])):
        if (x, y) not in flashed:
          octopi[y][x] += 1

  # Check if every octopi flashed
  if len(flashed) == ( len(octopi) * len(octopi[0])):
    done = True

print(f'All octopi will flash at step {step}.')