
# Parse the input from the input file
input_file = 'example_input.txt'
fish = []

with open(input_file) as input:
  input = input.readline()
  for f in input.split(','):
    fish.append(int(f))


# Task 1

# Simulate for 80 days
for day in range(80):
  new_fish = []

  for f in fish:
    # Reduce timer by 1
    if f != 0:
      new_fish.append(f-1)
    
    # Create new fish and reset timer
    else:
      new_fish.extend([6, 8])

  # Update fish list
  fish.clear()
  fish.extend(new_fish)

print(f'After 80 days there will be {len(fish)} lanternfish.')
print()


# Task 2

# The above method won't work when simulating for a total of 256 days
# (Exponential slowdown and the list will fill the memory)

# Lets make a list where index 0 will have a count of all fish with their counter at 0 
# index 1 will have a count of all fish with their counter at 1 and so on
compressed_fish = [0] * 9

for f in fish:
  compressed_fish[f] += 1

# Now simulate the ramaining 176 days
for day in range(176):
  new_compressed_fish = [0] * 9
  
  # Reduce the timer by 1
  for i, count in enumerate(compressed_fish):
    new_compressed_fish[i-1] += count

  # Above loop moves the fish in index 0 to index 8 (tecnically creating the new fish)
  # Add the fish from index 0 to index 6
  new_compressed_fish[6] += compressed_fish[0]

  # Update compressed_fish
  compressed_fish.clear()
  compressed_fish.extend(new_compressed_fish)

# Count the total fish
fish_count = 0

for count in compressed_fish:
  fish_count += count

print(f'After 256 days there will be {fish_count} lanternfish.')