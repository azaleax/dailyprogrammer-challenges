from enum import Enum

#TODO logic cleanup
#TODO code clean up & refactoring
#TODO remove debug print statements
#TODO make the code generic to account for both directions
#TODO allow starting location as an input... currently, encoding always starts at top-right

class Directions(Enum):
  CLOCKWISE         = 0
  COUNTER_CLOCKWISE = 1

# Populate the encoder array
def populate_encoder_array(string, encoder_array):
  string_idx = 0

  for row in range(len(encoder_array)):
    for column in range(len(encoder_array[row])):
      if (string_idx < len(string)):
        encoder_array[row][column] = string[string_idx]
        string_idx += 1
      else:
        break

# Create one loop for string
# TODO This function is messy & hardcoded to a certain extent... need to clean up the logic
def encode_clockwise_loop(
  string,
  encoder_array,
  is_encoded_array,
  loop_idx,
  start_row,
  start_column
  ):

  out_string = ''
  column = start_column
  is_encoding_done = False
  end_row = 0
  end_column = 0
  num_row = len(encoder_array)
  num_column = len(encoder_array[0])

  for row in range(loop_idx, (num_row - loop_idx)):
    if is_encoded_array[row][column] == True:
      is_encoding_done = True
      break
    out_string = out_string + encoder_array[row][column]
    is_encoded_array[row][column] = True
    print("row: " + str(row) + " column: " + str(column) + " " + out_string)
    end_row = row
  print()
  for column in reversed(range(loop_idx, (num_column - loop_idx) - 1)):
    if is_encoded_array[row][column] == True:
      is_encoding_done = True
      break
    out_string = out_string + encoder_array[row][column]
    is_encoded_array[row][column] = True
    print("row: " + str(row) + " column: " + str(column) + " " + out_string)
    end_column = column
  print()
  for row in reversed(range(loop_idx, (num_row - loop_idx) - 1)):
    if is_encoded_array[row][column] == True:
      is_encoding_done = True
      break
    out_string = out_string + encoder_array[row][column]
    is_encoded_array[row][column] = True
    print("row: " + str(row) + " column: " + str(column) + " " + out_string)
    end_row = row
  print()
  for column in range(loop_idx + 1, (num_column - loop_idx) - 1):
    if is_encoded_array[row][column] == True:
      is_encoding_done = True
      break
    out_string = out_string + encoder_array[row][column]
    is_encoded_array[row][column] = True
    print("row: " + str(row) + " column: " + str(column) + " " + out_string)
    end_column = column
  print()

  return out_string, is_encoding_done


# Encode for clockwise direction
def encode_clockwise(string, encoder_array, is_encoded_array):
  # Always start encoding at top-right
  loop_start_row = 0
  loop_start_column = len(encoder_array[0]) - 1
  loop_idx = 0
  loop_string = ''
  out_string = ''
  is_encoding_done = False

  while(is_encoding_done == False):  
    loop_string, is_encoding_done = encode_clockwise_loop(
      string,
      encoder_array,
      is_encoded_array,
      loop_idx,
      (loop_start_row + loop_idx),
      (loop_start_column - loop_idx),
      )

    out_string = out_string + loop_string

    print(out_string)
    loop_idx += 1

  return out_string


# Given input string, return route-cipher encoded string
def encode(inp_string, dimension, direction):
  # Remove any non-alphanumeric characters and convert the strint to all upper case
  stripped_string = ''.join(char for char in inp_string if char.isalnum()).upper()

  print(stripped_string)

  # Create and populate the array with the stripped string
  encoder_array = [['X' for column in range(dimension[0])] for row in range(dimension[1])]

  #Create and populate the array which contains the information whether the element in the array
  #has already been added in the encoded string
  is_encoded_array = [[False for column in range(dimension[0])] for row in range(dimension[1])]

  populate_encoder_array(stripped_string, encoder_array)

  print(encoder_array)

  out_string = ''

  #loop through the array in the given spiral direction
  if (direction == Directions.CLOCKWISE):
    out_string = encode_clockwise(stripped_string, encoder_array, is_encoded_array)
  elif (direction == Directions.COUNTER_CLOCKWISE):
    out_string = encode_counter_clockwise(stripped_string, encoder_array, is_encoded_array)
  else:
    assert(False)

  return out_string

# Run the encode function
out_string = encode("WE ARE DISCOVERED. FLEE AT ONCE", (9, 3), Directions.CLOCKWISE)

print(out_string)