from enum import Enum

#TODO logic cleanup
#TODO code clean up & refactoring
#TODO remove debug print statements
#TODO make the code generic to account for both directions
#TODO allow starting location as an input... currently, encoding always starts at top-right

class Location(object):
  def __init__(self, row, col):
    self.row = row
    self.col = col

  def __eq__(self, other):
    return (self.row == other.row and elf.col == other.col)

  def set_loc(row, col):
    self.row = row
    self.col = col

class Spiral_Directions(Enum):
  CLOCKWISE         = 0
  COUNTER_CLOCKWISE = 1

class Traverse_Directions(Enum):
  UP                = 0
  DOWN              = 1
  RIGHT             = 2
  LEFT              = 3

# Populate the encoder array
def populate_encoder_array(string, encoder_array):
  column_size = len(encoder_array[0])

  for i, char in enumerate(string):
    encoder_array[int(i / column_size)][int(i % column_size)] = char

# Traverse based on direction
def traverse(
  start_loc,
  end_loc,
  traverse_dir
  ):

  if (traverse_dir == Traverse_Directions.RIGHT):
    for col in range(start_loc.col, end_loc.col):
      out_string += encoder_array[start_loc.row][col]

  elif (traverse_dir == Traverse_Directions.DOWN):
    for row in range(start_loc.row, end_loc.row):
      out_string += encoder_array[row][start_loc.col]

  elif (traverse_dir == Traverse_Directions.LEFT):
    for col in reversed(range(end_loc.col, start_loc.col)):
      out_string += encoder_array[start_loc.row][col]

  elif (traverse_dir == Traverse_Direction.UP):
    for row in reversed(range(end_loc.row, start_loc.row)):
      out_string += encoder_array[row][start_loc.col]

  assert(start_loc == end_loc)

  return out_string

# Create one loop for string
# TODO This function is messy & hardcoded to a certain extent... need to clean up the logic
def encode_loop(
  encoder_array,
  loop_idx,
  start_loc,
  spiral_dir
  ):

  out_string = ''
  is_encoding_done = False

  #clockwise implementation first

  end_loc = Location(start_loc.row, len(encoder_array)
  out_string += traverse(start_loc, Traverse_Directions.DOWN,)

  return out_string, is_encoding_done


# Encode for clockwise direction
def encode_spiral(string, encoder_array, is_encoded_array, spiral_dir):
  # Always start encoding at top-right
  loop_start_loc = Location(0, len(encoder_array[0]) - 1)
  loop_idx = 0
  loop_string = ''
  out_string = ''
  is_encoding_done = False

  # TODO Remove this assert once counter_clockwise is implemented
  assert(spiral_dir == Spiral_Directions.CLOCKWISE)

  while(is_encoding_done == False):  
    loop_string, is_encoding_done = encode_loop(
      encoder_array,
      loop_idx,
      loop_start_loc,
      spiral_dir
      )

    out_string = out_string + loop_string

    loop_start_loc.set_loc(
      loop_start_loc.row + loop_idx,
      loop_start_loc.col - loop_idx
      )

    print(out_string)
    loop_idx += 1

  return out_string


# Given input string, return route-cipher encoded string
def encode(inp_string, dimension, spiral_dir):
  # Remove any non-alphanumeric characters and convert the strint to all upper case
  stripped_string = ''.join(char for char in inp_string if char.isalnum()).upper()

  # Create and populate the array with the stripped inp_string
  encoder_array = [ [ 'X' for column in range(dimension[0]) ]
                    for row in range(dimension[1]) ]

  populate_encoder_array(stripped_string, encoder_array)

  out_string = ''

  #loop through the array in the given spiral direction
  out_string = encode_spiral(
                  stripped_string,
                  encoder_array,
                  spiral_dir)

  return out_string