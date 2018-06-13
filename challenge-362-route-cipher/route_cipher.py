from enum import Enum

#TODO allow starting location as an input... currently, encoding always starts at top-right

class Location(object):
  def __init__(self, row, col):
    self.row = row
    self.col = col

  def __eq__(self, other):
    return (self.row == other.row and self.col == other.col)

  def __str__(self):
    return ('(' + str(self.row) + ', ' + str(self.col) + ')')

  def set_loc(self, row, col):
    self.row = row
    self.col = col

  def step(self, traverse_dir):
    if (traverse_dir == Traverse_Directions.RIGHT):
      self.col += 1
    elif (traverse_dir == Traverse_Directions.DOWN):
      self.row += 1
    elif (traverse_dir == Traverse_Directions.LEFT):
      self.col -= 1
    elif (traverse_dir == Traverse_Directions.UP):
      self.row -= 1

class Spiral_Directions(Enum):
  CLOCKWISE         = 0
  COUNTER_CLOCKWISE = 1

class Traverse_Directions(Enum):
  UP                = 0
  DOWN              = 1
  RIGHT             = 2
  LEFT              = 3
  NUM_DIRECTIONS    = 4

direction_order = [
  [
    Traverse_Directions.DOWN,
    Traverse_Directions.LEFT,
    Traverse_Directions.UP,
    Traverse_Directions.RIGHT,
  ],
  [
    Traverse_Directions.LEFT,
    Traverse_Directions.DOWN,
    Traverse_Directions.RIGHT,
    Traverse_Directions.UP,
  ], 
]

IS_CHAR_DECODED = ' '

# Populate the encoder array
def populate_encoder_array(string, encoder_array):
  column_size = len(encoder_array[0])

  for i, char in enumerate(string):
    encoder_array[int(i / column_size)][int(i % column_size)] = char


# Traverse based on direction
def traverse(
  encoder_array,
  loc,
  num_steps,
  traverse_dir
  ):

  out_string = ''

  for step in range(num_steps):
    if encoder_array[loc.row][loc.col] == IS_CHAR_DECODED:
      break

    out_string += encoder_array[loc.row][loc.col]
    encoder_array[loc.row][loc.col] = IS_CHAR_DECODED
    loc.step(traverse_dir)

  return out_string


# Create one loop for string
def encode_loop(
  encoder_array,
  loop_idx,
  loc,
  spiral_dir
  ):

  out_string = ''
  num_vertical_steps = len(encoder_array) - ((2 * loop_idx) + 1)
  num_horizontal_steps = len(encoder_array[0]) - ((2 * loop_idx) + 1)

  for idx in range(Traverse_Directions.NUM_DIRECTIONS.value):
    if (direction_order[spiral_dir.value][idx] == Traverse_Directions.UP or
        direction_order[spiral_dir.value][idx] == Traverse_Directions.DOWN):
          num_steps = num_vertical_steps
    else:
      num_steps = num_horizontal_steps

    traversed_string = traverse(
      encoder_array,
      loc,
      num_steps,
      direction_order[spiral_dir.value][idx]
      )

    out_string += traversed_string

  return out_string


# Encode for clockwise direction
def encode_spiral(string, encoder_array, spiral_dir):
  # Always start encoding at top-right
  loop_start_loc = Location(0, len(encoder_array[0]) - 1)
  loop_idx = 0
  loop_string = ''
  out_string = ''

  while(True):

    out_string = out_string + loop_string

    loop_string = encode_loop(
      encoder_array,
      loop_idx,
      loop_start_loc,
      spiral_dir
      )

    loop_idx += 1

    loop_start_loc.set_loc(
      loop_start_loc.row + 1,
      loop_start_loc.col - 1
      )

    if (loop_string == ''):
      break

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