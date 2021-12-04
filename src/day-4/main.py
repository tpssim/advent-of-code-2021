
# Parse the input from the input file
input_file = 'example_input.txt'
draw_sequence = []
tables = []

with open(input_file) as input:

  draw_sequence = list(input.readline().rstrip().split(','))

  table = []
  for line in input.readlines():
    if line.isspace() and table != []:
      tables.append(table)
      table = []
    else:
      table.extend(list(line.rstrip().split()))
  
  # If there is no empty line at the end of the input file
  if table != []:
    tables.append(table)



# Return True if table has bingo with numbers_drawn
# False otherwise
def checkBingo(table, numbers_drawn):

  # Rows
  if (
    all(num in numbers_drawn for num in table[0:5]) or
    all(num in numbers_drawn for num in table[5:10]) or
    all(num in numbers_drawn for num in table[10:15]) or
    all(num in numbers_drawn for num in table[15:20]) or
    all(num in numbers_drawn for num in table[20:25])
    ):
    return True

  # Columns
  if (
    all(num in numbers_drawn for num in table[0::5]) or
    all(num in numbers_drawn for num in table[1::5]) or
    all(num in numbers_drawn for num in table[2::5]) or
    all(num in numbers_drawn for num in table[3::5]) or
    all(num in numbers_drawn for num in table[4::5])
    ):
    return True

  return False


# Calculate the score for table with numbers_drawn
def getScore(table, numbers_drawn):
  score = 0

  for num in table:
    if num not in numbers_drawn:
      score += int(num)

  return score * int(numbers_drawn[-1])


# Task 1

numbers_drawn = []
winning_table = 0
winning_score = 0
done = False

for num in draw_sequence:
  if done: 
    break

  # Draw a number 
  numbers_drawn.append(num)

  # Check for bingo
  for i, table in enumerate(tables):
    if checkBingo(table, numbers_drawn):
      winning_score = getScore(table, numbers_drawn)
      winning_table = i
      done = True
      break

print(f'The table with index {winning_table} wins with a score of: {winning_score}')
print()


# Task 2

numbers_drawn = []
total_tables = len(tables)
winners = []
winner_count = 0
losing_table = 0
losing_score = 0
done = False

for num in draw_sequence:
  if done: 
    break

  # Draw a number 
  numbers_drawn.append(num)

  for i, table in enumerate(tables):
    # Skip if table has already won
    if i in winners:
      continue
    
    # Check for bingo
    if checkBingo(table, numbers_drawn):
      winners.append(i)
      winner_count += 1

      # Check if last
      if winner_count == total_tables:
        losing_score = getScore(table, numbers_drawn)
        losing_table = i
        done = True
        break

print(f'The table with index {losing_table} will lose with a score of: {losing_score}')