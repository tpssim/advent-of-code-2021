
# Parse the input from the input file
input_file = 'example_input.txt'
positions = []

with open(input_file) as input:
  input = input.readline()
  for f in input.split(','):
    positions.append(int(f))


# Task 1

max_pos = max(positions)

# Calculate the ful cost for all positions from 0 to max_pos
fuel_costs = [0] * (max_pos + 1)

for i in range(max_pos + 1):
  for pos in positions:
    fuel_costs[i] += abs(i - pos)

# Find lovest cost position and the fuel cost for it
lowest_cost = min(fuel_costs)
lowest_cost_pos = fuel_costs.index(lowest_cost)

print(f'Cheapest position to aling to is {lowest_cost_pos}, with a fuel cost of {lowest_cost}.')
print()


# Task 2

# Calculate the ful cost for all positions from 0 to max_pos
# Each moved step burns 1 more fuel than the previous one
fuel_costs = [0] * (max_pos + 1)

for i in range(max_pos + 1):
  for pos in positions:
    distance = abs(i - pos)
    fuel_costs[i] += ((distance + 1) / 2) * distance

# Find lovest cost position and the fuel cost for it
lowest_cost = min(fuel_costs)
lowest_cost_pos = fuel_costs.index(lowest_cost)

print('Using the newly aquired information of how crab submarines burn fuel.')
print(f'Cheapest position to aling to is {lowest_cost_pos}, with a fuel cost of {lowest_cost}.')