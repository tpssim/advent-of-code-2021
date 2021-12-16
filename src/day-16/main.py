
# Parse the input from the input file
input_file = 'example_input.txt'
packet = ''

with open(input_file) as input:
  packet = input.readline()

# Convert the packet to array of bits
# Add 1 to the start and remove it to keep leading zeroes
packet = int('1' + packet, 16)
packet = list(bin(packet)[3:])


# Task 1

# Pop multiple items from start of an array
def multipop(arr, amount):
  popped = []
  for i in range(amount):
    popped.append(arr.pop(0))

  return popped

# Convert array of bits to integer
def toInt(arr):
  return int(''.join(arr), 2)

# Read the packet data

version_sum = 0
decoded_packets = []

while not all([bit == '0' for bit in packet]):

  decoded_packet = {}

  # Packet version
  version = multipop(packet, 3)
  version = toInt(version)

  # Increment version sum
  version_sum += version

  # Packet type ID
  type_ID = multipop(packet, 3)
  type_ID = toInt(type_ID)

  decoded_packet.update({'version': version, 'type_ID': type_ID})

  # ID 4 is a literal value
  if type_ID == 4:

    literal = []
    done = False
    length = 6

    while not done:

      group = multipop(packet, 5)
      literal.extend(group[1:])
      length += 5

      if group[0] == '0':
        done = True

    literal = toInt(literal)

    decoded_packet.update({'literal': literal, 'length': length})

  # Every other ID is an operator
  else: 

    length_type_ID = packet.pop(0)
    decoded_packet.update({'length_type_ID': length_type_ID})

    # ID 0 means length is a 15-bit number representing the number of bits in the sub-packets
    if length_type_ID == '0':

      length = multipop(packet, 15)
      length = toInt(length)
      decoded_packet.update({'length': length})

    # ID 1 means length is a 11-bit number representing the number of sub-packets  
    else:

      length = multipop(packet, 11)
      length = toInt(length)
      decoded_packet.update({'length': length})

  decoded_packets.append(decoded_packet)

print(f'Sum of all version numbers in the packets: {version_sum}')
print()


# Task 2

# Evaluate decoded packets
result = 0

# Recursively evaluate packets
def evalPackets(packets):
  packet = packets.pop(0)

  # Literal value
  if packet.get('type_ID') == 4:
    return (packet.get('literal'), packet.get('length'))

  operands = []
  length = 0


  # length is a number representing the number of bits in the sub-packets
  if packet.get('length_type_ID') == '0':

    length = packet.get('length')
    length_count = 0

    while length_count < length:

      val, len = evalPackets(packets)

      operands.append(val)
      length_count += len

    # Length of length field
    length += 15

  # length is a number representing the number of sub-packets
  else:

    for i in range(packet.get('length')):

      val, len = evalPackets(packets)

      operands.append(val)
      length += len

    # Length of length field
    length += 11

  # Header of operator is 7 bits
  length += 7


  # Sum of operands
  if packet.get('type_ID') == 0:

    return (sum(operands), length)

  # Product of operands
  elif packet.get('type_ID') == 1:
    
    prod = 1
    for x in operands:
      prod = prod * x

    return (prod, length)
  
  # Minimum operand
  elif packet.get('type_ID') == 2:
    
    return (min(operands), length)
  
  # Maximum operand
  elif packet.get('type_ID') == 3:
    
    return (max(operands), length)
  
  # Greater than
  elif packet.get('type_ID') == 5:
    
    result = 1 if operands[0] > operands[1] else 0

    return (result, length)

  # Less than
  elif packet.get('type_ID') == 6:

    result = 1 if operands[0] < operands[1] else 0

    return (result, length)

  # Equal to
  elif packet.get('type_ID') == 7:
    
    result = 1 if operands[0] == operands[1] else 0

    return (result, length)


result, len = evalPackets(decoded_packets)

print(f'Result of the evaluated expression: {result}')